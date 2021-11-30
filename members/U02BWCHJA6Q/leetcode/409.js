/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  const map = new Map();
  let count = 0;

  for (let c of s) {
    if (map.has(c)) {
      map.delete(c);
      count++;
    } else {
      map.set(c, 1);
    }
  }

  return map.size > 0 ? 2 * count + 1 : 2 * count;
};
