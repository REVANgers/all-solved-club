/**
 * @param {string} s
 * @return {string[]}
 */
var findRepeatedDnaSequences = function (s) {
  const set = new Set();
  const repeated = new Set();

  for (let i = 0; i <= s.length - 10; i++) {
    const current = s.slice(i, i + 10);

    if (set.has(current)) {
      repeated.add(current);

      continue;
    }

    set.add(current);
  }

  return [...repeated];
};
