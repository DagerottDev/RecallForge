import assert from 'node:assert/strict';
import path from 'node:path';

export async function checkSamples(browser, output) {
  const context = await browser.newContext({ viewport: {width:1440, height:900} });
  const page = await context.newPage(), requests = [], errors = [];
  page.on('request', request => { if (/^https?:/.test(request.url())) requests.push(request.url()); });
  page.on('pageerror', error => errors.push(error.message));
  try {
    await page.goto(new URL('../mcq-exam-website/index.html', import.meta.url).href);
    await page.locator('#appearance-open').waitFor({state:'attached'});
    assert.equal(await page.locator('#sample-pack').inputValue(), 'biology');
    for (const [name, title, count] of [['biology','Cell Biology',9],['cfa','CFA Fundamentals',10],['cmt','CMT Technical Analysis',10],['frm','FRM Risk Concepts',10]]) {
      await page.locator('#sample-pack').selectOption(name);
      await page.locator('#load-sample-btn').click();
      await page.locator('#exam-view').waitFor({state:'visible'});
      assert.ok((await page.locator('#exam-title').innerText()).includes(title));
      assert.equal(await page.locator('#palette button').count(), count);
      if (name !== 'biology') {
        assert.match(await page.locator('#exam-instructions').innerText(), /not official/);
        const raw = JSON.parse(await page.locator(`#embedded-sample-${name}`).textContent());
        await page.locator('.option').nth(raw.questions[0].answerIndex).click();
        await page.locator('#check-btn').click();
        assert.match(await page.locator('#study-feedback').innerText(), /^Correct/);
        assert.equal(await page.locator('#study-feedback a').getAttribute('href'), raw.questions[0].sourceRefs[0]);
        await page.keyboard.press('ArrowRight');
        assert.match(await page.locator('#question-number').innerText(), /2 of 10/);
      }
      await page.screenshot({path:path.join(output, `sample-${name}.png`)});
      await page.locator('#submit-btn').click();
      await page.getByRole('dialog',{name:'Confirm action'}).getByRole('button',{name:'Continue'}).click();
      await page.locator('#result-view').waitFor({state:'visible'});
      await page.locator('#new-exam-btn').click();
    }
    await page.reload();
    await page.getByRole('button',{name:'Library',exact:true}).click();
    assert.equal(await page.locator('.library-row').count(), 4, 'Sample changes must preserve earlier packs');
    await page.getByRole('button',{name:'Progress',exact:true}).click();
    assert.equal(await page.locator('[data-open-attempt]').count(), 4, 'Sample changes must preserve earlier attempts');
    await page.getByRole('button',{name:'Home',exact:true}).click();
    await page.locator('#sample-pack').selectOption('cfa');
    await page.locator('#load-sample-btn').click();
    await page.locator('#exam-view').waitFor({state:'visible'});
    await page.locator('#submit-btn').click();
    await page.getByRole('dialog',{name:'Confirm action'}).getByRole('button',{name:'Continue'}).click();
    await page.locator('#result-view').waitFor({state:'visible'});
    await page.locator('#new-exam-btn').click();
    await page.getByRole('button',{name:'Library',exact:true}).click();
    assert.equal(await page.locator('.library-row').count(), 4, 'Reimported samples must deduplicate');
    assert.deepEqual(requests, [], 'Embedded samples must work without network resources');
    assert.deepEqual(errors, []);
    console.log('samples: four offline packs, correct feedback, keyboard navigation, reload preservation and reimport deduplication passed');
  } finally { await context.close(); }
}
