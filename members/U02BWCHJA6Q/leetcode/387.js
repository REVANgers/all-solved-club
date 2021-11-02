/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  const map = new Map();
  const set = new Set();

  for (let i = 0; i < s.length; i++) {
    const c = s[i];

    if (map.has(c)) {
      map.delete(c);
      continue;
    }
    if (set.has(c)) {
      continue;
    }

    set.add(c);
    map.set(c, i);
  }

  if (map.size === 0) {
    return -1;
  }

  return [...map][0][1];
};
