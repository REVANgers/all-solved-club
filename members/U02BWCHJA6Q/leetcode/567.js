/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  if (s1 === '' || s2 === '') {
    return false;
  }
  let map = new Map();

  for (let i = 0; i < s1.length; i++) {
    map.set(s1[i], map.get(s1[i]) + 1 || 1);
  }
  let start = 0,
    windowSize = s1.length;
  let counter = map.size;

  for (let end = 0; end < s2.length; end++) {
    let char = s2[end];
    if (map.has(char)) {
      map.set(char, map.get(char) - 1);
    }
    if (map.get(char) === 0) {
      counter--;
    }
    while (counter === 0) {
      if (end - start + 1 === windowSize) {
        return true;
      }
      if (map.has(s2[start])) {
        map.set(s2[start], map.get(s2[start]) + 1);
      }
      if (map.get(s2[start]) === 1) {
        counter++;
      }
      start++;
    }
  }
  return false;
};
