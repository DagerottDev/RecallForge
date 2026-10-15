import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';

const root = 'https://dagerottdev.github.io/RecallForge/';
test('public discovery metadata describes the app and FAQ answers match visible content', async () => {
  const app = await readFile(new URL('../src/index.html', import.meta.url), 'utf8');
  const guide = await readFile(new URL('../src/about.html', import.meta.url), 'utf8');
  const schema = html => JSON.parse(html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/)[1]);
  assert.equal(schema(app).url, root);
  assert.equal(schema(app).isAccessibleForFree, true);
  assert.ok(!/<script(?! type="application\/ld\+json")/i.test(guide), 'guide remains readable without app JavaScript');
  const plain = guide.replace(/<[^>]+>/g, '').replace(/\s+/g, ' ');
  for (const question of schema(guide).mainEntity) {
    assert.ok(plain.includes(question.name));
    assert.ok(plain.includes(question.acceptedAnswer.text));
  }
  const sitemap = await readFile(new URL('../src/sitemap.xml', import.meta.url), 'utf8');
  assert.deepEqual([...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map(match => match[1]), [root, `${root}about.html`]);
});
