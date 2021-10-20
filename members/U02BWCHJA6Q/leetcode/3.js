/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let set = new Set();
  let start = 0;
  let max = 0;

  for (let end = 0; end < s.length; end++) {
    while (set.has(s[end])) {
      set.delete(s[start++]);
    }
    set.add(s[end]);
    max = Math.max(max, end - start + 1);
  }
  return max;
};
