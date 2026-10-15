import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import { build } from 'esbuild';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = (file) => readFile(path.join(root, file), 'utf8');
const [template, styles, sampleRaw, license, bundle] = await Promise.all([
  read('src/index.html'), read('src/styles.css'), read('mcq-exam-website/sample-mcq-pack.json'), read('LICENSE'),
  build({ entryPoints: [path.join(root, 'src/app.js')], bundle: true, write: false, format: 'iife', target: 'es2022', legalComments: 'inline', loader: { '.ttf': 'dataurl' } }),
]);
let css = styles;
for (const [name, file] of [['Source Sans 3','SourceSans3'],['Lexend','Lexend'],['Atkinson Hyperlegible','AtkinsonHyperlegible'],['Lora','Lora']]) {
  const bytes = await readFile(path.join(root, `src/assets/fonts/${file}.ttf`));
  css = `@font-face{font-family:'${name}';src:url(data:font/ttf;base64,${bytes.toString('base64')}) format('truetype');font-weight:100 900;font-display:swap}\n${css}`;
}
const pdfLicense = await read('node_modules/pdfjs-dist/LICENSE');
const brandIcon = (await readFile(path.join(root, 'src/assets/branding/recallforge-mark.png'))).toString('base64');
const notices = await Promise.all(['sourcesans3','lexend','atkinsonhyperlegible','lora'].map(f => read(`src/assets/fonts/${f}-LICENSE.txt`)));
const safeScript = (s) => s.replace(/<\/script/gi, '<\\/script');
let sampleTemplate = template;
for (const [name, file] of [['CFA','cfa-fundamentals'],['CMT','cmt-technical-analysis'],['FRM','frm-risk-concepts']]) {
  const sample = await read(`mcq-exam-website/samples/${file}.json`);
  sampleTemplate = sampleTemplate.replace(`__${name}_SAMPLE__`, () => safeScript(JSON.stringify(JSON.parse(sample))));
}
const worker = await read('node_modules/pdfjs-dist/build/pdf.worker.mjs');
const output = sampleTemplate.replace('<!doctype html>', () => `<!doctype html>\n<!--\n${license.trim()}\nPDF.js license:\n${pdfLicense}\nFont notices:\n${notices.join('\n').replaceAll('--','—')}\n-->`)
  .replace('<link rel="stylesheet" href="./styles.css">', () => `<style>\n${css}\n</style>`)
  .replaceAll('./assets/branding/recallforge-mark.png', `data:image/png;base64,${brandIcon}`)
  .replace('__SAMPLE_PACK__', () => safeScript(JSON.stringify(JSON.parse(sampleRaw))))
  .replace('<script type="module" src="./app.js"></script>', () => `<script>\n${safeScript(`globalThis.__EXAM_PDF_WORKER__=${JSON.stringify(worker)};\n${bundle.outputFiles[0].text}`)}\n</script>`);
const artifacts = [
  ['index.html', Buffer.from(output)],
  ...await Promise.all(['about.html', 'llms.txt', 'sitemap.xml', 'styles.css'].map(async file => [file, await readFile(path.join(root, 'src', file))])),
  ['recallforge.png', await readFile(path.join(root, 'src/assets/branding/recallforge-mark.png'))],
];
const checking = process.argv.includes('--check');
const stale = [];
for (const [file, bytes] of artifacts) {
  const target = path.join(root, 'mcq-exam-website', file);
  if (checking) {
    if (!(await readFile(target).catch(() => Buffer.alloc(0))).equals(bytes)) stale.push(file);
  } else await writeFile(target, bytes);
}
if (stale.length) { console.error(`Distribution is stale (${stale.join(', ')}). Run npm run build.`); process.exit(1); }
console.log(checking ? 'Offline viewer and public discovery files are up to date.' : `Built offline viewer (${Buffer.byteLength(output)} bytes) and public discovery files.`);
