/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const map = new Map();

  strs.forEach(str => {
    const key = str
      .split('')
      .sort((a, b) => (a < b ? -1 : 1))
      .join('');

    if (map.has(key)) {
      map.get(key).push(str);

      return;
    }

    map.set(key, [str]);
  });

  return [...map].map(([_, v]) => v);
};
