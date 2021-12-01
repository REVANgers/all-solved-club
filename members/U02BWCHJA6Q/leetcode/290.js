/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function (pattern, s) {
  const words = s.split(' ');
  const map = new Map();

  if (pattern.length !== words.length) {
    return false;
  }

  if (new Set(pattern).size !== new Set(words).size) {
    return false;
  }

  return words.every((word, index) => {
    if (!map.has(word)) {
      map.set(word, pattern[index]);

      return true;
    }

    return map.get(word) === pattern[index];
  });
};
