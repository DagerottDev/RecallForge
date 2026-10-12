import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { validatePack, preparePack, createSession, setAnswer, scoreExam } from '../src/core/exam-engine.js';

const packs = {};
for (const name of ['cfa-fundamentals','cmt-technical-analysis','frm-risk-concepts']) {
  packs[name] = JSON.parse(await readFile(new URL(`../mcq-exam-website/samples/${name}.json`, import.meta.url)));
}

test('finance demos validate, have ten original sourced questions, and score correctly', () => {
  for (const raw of Object.values(packs)) {
    assert.deepEqual(validatePack(raw), []);
    assert.equal(raw.questions.length, 10);
    assert.equal(new Set(raw.questions.map(q => q.question)).size, 10);
    assert.equal(raw.exam.totalMarks, 10);
    assert.match(raw.exam.difficultyNote, /not calibrated/);
    for (const q of raw.questions) {
      assert.ok(q.explanation && q.learningObjective);
      assert.ok(q.sourceRefs.every(ref => new URL(ref).protocol === 'https:'));
      assert.equal(q.negativeMarks, 0);
    }
    const pack = preparePack(raw), session = createSession(pack, 0);
    for (const q of pack.questions) setAnswer(session, q.id, q.answerIndex);
    assert.equal(scoreExam(pack, session).earned, 10);
  }
});

test('finance demonstration numerical answers agree with independent calculations', () => {
  const answer = (name, id) => { const q = packs[name].questions.find(q => q.id === id); return q.options[q.answerIndex]; };
  const numeric = (name, id) => Number(answer(name, id).replaceAll(',', '').replace('%', ''));
  assert.equal(numeric('cfa-fundamentals', 1), Math.round(10000 * 1.05 ** 2));
  assert.equal(numeric('cfa-fundamentals', 2), Math.round(1210 / 1.1 ** 2));
  assert.equal(numeric('cfa-fundamentals', 3), (110 - 100 + 5) / 100 * 100);
  assert.equal(numeric('cfa-fundamentals', 4), 0.6 * 10 + 0.4 * 5);
  assert.equal(numeric('cmt-technical-analysis', 1), (10 + 12 + 14) / 3);
  assert.equal(numeric('cmt-technical-analysis', 2), (12 + 14 + 16) / 3);
  assert.equal(numeric('frm-risk-concepts', 1), 0.02 * 0.4 * 100000);
  assert.equal(numeric('frm-risk-concepts', 2), 100 - 60);
  assert.equal(numeric('frm-risk-concepts', 3), 0.5 * 0 + 0.3 * 1000 + 0.2 * 5000);
  assert.equal(answer('frm-risk-concepts', 4), `${6 - 2}% to ${6 + 2}%`);
});
