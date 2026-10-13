"""Render RecallForge's eight campaign videos from actual app captures and local Kokoro speech.

Run with output/promotion/.venv/bin/python; media dependencies are separate from the app.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import textwrap

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps
import soundfile as sf

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/promotion'
CAPTURES = OUT / 'captures'
ASSETS = OUT / 'assets'
FONT = ROOT / 'src/assets/fonts/SourceSans3.ttf'
INK = '#111923'
WHITE = '#edf2f8'
MUTED = '#adbdcf'
RATE = 24000
VOICE = 'af_heart'
SPEED = 1.10
pipeline = None


def logo(image, position, size):
    mark = Image.open(ROOT / 'src/assets/branding/recallforge-master.png').convert('RGBA')
    mark = mark.resize((size, size), Image.Resampling.LANCZOS)
    image.paste(mark, position, mark)


def font(size):
    face = ImageFont.truetype(str(FONT), size)
    face.set_variation_by_axes([500])
    return face


def lines(text, size, width):
    result, line = [], ''
    for word in text.split():
        candidate = (line + ' ' + word).strip()
        if line and font(size).getlength(candidate) > width:
            result.append(line)
            line = word
        else:
            line = candidate
    if line:
        result.append(line)
    return '\n'.join(result)


def artwork():
    ASSETS.mkdir(parents=True, exist_ok=True)
    avatar = Image.open(ROOT / 'src/assets/branding/recallforge-master.png').convert('RGBA')
    avatar = avatar.resize((800,800), Image.Resampling.LANCZOS)
    avatar.save(ASSETS / 'avatar.png')
    banner = Image.new('RGB', (2560,1440), INK)
    draw = ImageDraw.Draw(banner)
    draw.rectangle((0,490,2560,950), fill='#1b2635')
    logo(banner, (590,552), 200)
    draw.text((846,562), 'RecallForge', font=font(112), fill=WHITE)
    draw.text((851,706), 'Practice. Review. Remember.', font=font(56), fill='#9fc5ff')
    draw.text((851,804), 'Free & open source  ·  No account required', font=font(37), fill=MUTED)
    banner.save(ASSETS / 'banner.png')


def thumbnail(video):
    image = Image.new('RGB', (1280,720), INK)
    draw = ImageDraw.Draw(image)
    color = video['color']
    logo(image, (55,45), 80)
    draw.text((157,53), 'RecallForge', font=font(42), fill=WHITE)
    draw.text((57,157), 'QUICK TOUR' if video['week']==1 and not video['short'] else 'SHORT' if video['short'] else 'INTRODUCTORY PRACTICE', font=font(24), fill=color)
    headline = lines(video['thumbnailHeadline'], 67, 620)
    draw.multiline_text((55,218), headline, font=font(67), fill=WHITE, spacing=8)
    source = Image.open(CAPTURES / video['scenes'][min(1,len(video['scenes'])-1)]['image']).convert('RGB')
    draw.rounded_rectangle((740,85,1238,625), radius=20, fill='#1b2635', outline='#3a4c63', width=3)
    screenshot = ImageOps.contain(source, (464,505), Image.Resampling.LANCZOS)
    image.paste(screenshot, (757+(464-screenshot.width)//2,100+(505-screenshot.height)//2))
    draw.text((57,628), 'Free browser app  ·  Open source', font=font(28), fill=MUTED)
    image.save(ASSETS / f"{video['id']}-thumbnail.png")


def frame(video, scene, caption, step):
    short = video['short']
    image = Image.new('RGB', (1080,1920) if short else (1920,1080), INK)
    draw = ImageDraw.Draw(image)
    color = video['color']
    logo(image, (39,33), 80)
    draw.text((140,39), 'RecallForge', font=font(46), fill=WHITE)
    draw.text((140,92), 'INTRODUCTORY DEMO' if video['week']>1 else 'FREE STUDY WORKSPACE', font=font(23), fill=color)
    source = Image.open(CAPTURES / scene['image']).convert('RGB')
    if short:
        draw.multiline_text((40,155), lines(scene['title'], 66, 980), font=font(66), fill=WHITE, spacing=2)
        # The responsive app is reframed, rather than shrinking a desktop view into a Short.
        source = source.crop((0,240,source.width,min(source.height,890)))
        box = (40,335,1040,1535)
    else:
        draw.multiline_text((40,210), lines(scene['title'], 58, 340), font=font(58), fill=WHITE, spacing=7)
        draw.text((40,140), f"{step:02d} / {len(video['scenes']):02d}", font=font(30), fill=color)
        draw.multiline_text((40,640), 'Practice.\nReview.\nRemember.', font=font(40), fill=MUTED, spacing=8)
        box = (420,135,1880,910)
        if any(word in scene['image'] for word in ['question','feedback','mistake','recovery','rsi','retest']):
            source = source.crop((260,240,1370,min(source.height,825)))
    draw.rounded_rectangle(box, radius=14, fill='#1b2635', outline='#3a4c63', width=2)
    screenshot = ImageOps.contain(source, (box[2]-box[0]-12,box[3]-box[1]-12), Image.Resampling.LANCZOS)
    image.paste(screenshot, (box[0]+(box[2]-box[0]-screenshot.width)//2,box[1]+(box[3]-box[1]-screenshot.height)//2))
    if short:
        wrapped = lines(caption, 47, 990)
        assert len(wrapped.splitlines()) <= 4, 'Short caption overflows its safe area'
        draw.multiline_text((40,1570), wrapped, font=font(47), fill=WHITE, spacing=7)
        draw.text((40,1838), 'Try the free app · Link on channel profile', font=font(32), fill=color)
    else:
        size = 40
        while len(lines(caption,size,1810).splitlines()) > 2 and size > 30:
            size -= 2
        wrapped = lines(caption,size,1810)
        assert len(wrapped.splitlines()) <= 2, 'Landscape caption overflows its safe area'
        draw.multiline_text((45,944), wrapped, font=font(size), fill=WHITE, spacing=5)
    return image


def speech(text, directory):
    global pipeline
    digest = hashlib.sha256((VOICE+str(SPEED)+text).encode()).hexdigest()[:20]
    path = directory / f'{digest}.wav'
    if path.exists():
        audio, rate = sf.read(path, dtype='float32')
        assert rate == RATE
        return audio
    if pipeline is None:
        import torch
        from kokoro import KPipeline
        torch.set_num_threads(4)
        pipeline = KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M', device='cpu')
    chunks = [audio.numpy() for _,_,audio in pipeline(text, voice=VOICE, speed=SPEED)]
    assert chunks, f'No narration for: {text}'
    audio = np.concatenate(chunks)
    assert len(audio)>0 and np.isfinite(audio).all()
    assert np.max(np.abs(audio)) <= 1.01, 'Narration clipped'
    sf.write(path, audio, RATE)
    return audio


def stamp(seconds):
    milliseconds = round(seconds*1000)
    hours, milliseconds = divmod(milliseconds,3600000)
    minutes, milliseconds = divmod(milliseconds,60000)
    seconds, milliseconds = divmod(milliseconds,1000)
    return f'{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}'


def render(video):
    directory = OUT / video['id']
    directory.mkdir(parents=True,exist_ok=True)
    (directory/'frames').mkdir(exist_ok=True)
    (OUT/'speech').mkdir(exist_ok=True)
    timeline, sounds, captions = [], [], []
    elapsed = 0.0
    cue = 0
    for step, scene in enumerate(video['scenes'],1):
        sentences = re.split(r'(?<=[.!?])\s+',scene['narration'])
        scene_seconds = 0
        for sentence in sentences:
            audio = speech(sentence,OUT/'speech')
            duration = len(audio)/RATE
            cue += 1
            caption = sentence.replace('C F A','CFA').replace('C M T','CMT').replace('F R M','FRM').replace('Recall Forge','RecallForge')
            frame_path = directory/'frames'/f'{cue:03}.png'
            frame(video,scene,caption,step).save(frame_path)
            silence = 0.28
            timeline.append((frame_path,duration+silence))
            sounds.extend([audio,np.zeros(round(silence*RATE),dtype='float32')])
            captions.append(f'{cue}\n{stamp(elapsed)} --> {stamp(elapsed+duration)}\n'+ '\n'.join(textwrap.wrap(caption, 46 if video['short'] else 85))+'\n')
            elapsed += duration+silence
            scene_seconds += duration+silence
        gap = max(0,video['targetSeconds']/len(video['scenes'])-scene_seconds)
        if gap:
            timeline[-1] = (timeline[-1][0],timeline[-1][1]+gap)
            sounds.append(np.zeros(round(gap*RATE),dtype='float32'))
            elapsed += gap
        print(f"{video['id']} scene {step}/{len(video['scenes'])}: {elapsed:.1f}s",flush=True)
    audio = np.concatenate(sounds)
    sf.write(directory/'narration.wav',audio,RATE)
    (directory/'captions.srt').write_text('\n'.join(captions),encoding='utf-8')
    listing='ffconcat version 1.0\n'
    for file,duration in timeline:
        listing+=f"file 'frames/{file.name}'\nduration {duration:.6f}\n"
    listing+=f"file 'frames/{timeline[-1][0].name}'\n"
    (directory/'frames.ffconcat').write_text(listing)
    destination = directory/f"{video['id']}.mp4"
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-safe','0','-f','concat','-i',str(directory/'frames.ffconcat'),'-i',str(directory/'narration.wav'),'-i',str(directory/'captions.srt'),'-map','0:v','-map','1:a','-map','2:s','-af','loudnorm=I=-16:TP=-1.5:LRA=11','-c:v','libx264','-preset','fast','-crf','20','-r','30','-pix_fmt','yuv420p','-c:a','aac','-b:a','160k','-c:s','mov_text','-metadata:s:s:0','language=eng','-movflags','+faststart','-t',str(elapsed),str(destination)],check=True)
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(destination)]))
    stream=next(s for s in probe['streams'] if s['codec_type']=='video')
    expected=(1080,1920) if video['short'] else (1920,1080)
    assert (stream['width'],stream['height'])==expected
    assert any(s['codec_type']=='audio' for s in probe['streams'])
    assert any(s['codec_type']=='subtitle' for s in probe['streams'])
    assert abs(float(probe['format']['duration'])-elapsed)<0.2
    assert len(captions)>0
    assert elapsed <= (36 if video['short'] else 95 if video['week']==1 else 240), 'Narration exceeds the planned length'
    report=dict(id=video['id'],voice=VOICE,speed=SPEED,width=expected[0],height=expected[1],seconds=float(probe['format']['duration']),captionCues=cue,peak=float(np.max(np.abs(audio))),rms=float(math.sqrt(np.mean(audio**2))),source='Actual isolated app captures; original scripts; local Kokoro narration',sha256=hashlib.sha256(destination.read_bytes()).hexdigest())
    (directory/'validation.json').write_text(json.dumps(report,indent=2)+'\n')
    thumbnail(video)
    print('Rendered',destination,flush=True)


if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--only',help='Render one video ID from the campaign specification')
    args.add_argument('--artwork-only',action='store_true',help='Export channel artwork and thumbnails without regenerating narration or videos')
    args=args.parse_args()
    videos=json.loads((ROOT/'docs/promotion/videos.json').read_text())
    assert len(videos)==8 and len({v['id'] for v in videos})==8
    artwork()
    selected=[v for v in videos if not args.only or v['id']==args.only]
    assert selected, 'Unknown video ID'
    for video in selected:
        assert video['scenes'] and all((CAPTURES/s['image']).is_file() for s in video['scenes'])
        if args.artwork_only:
            thumbnail(video)
        else:
            render(video)
