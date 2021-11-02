/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const sCount = {};
  const tCount = {};

  for (let i = 0; i < s.length; i++) {
    sCount[s[i]] ? (sCount[s[i]] += 1) : (sCount[s[i]] = 1);
  }

  for (let i = 0; i < t.length; i++) {
    tCount[t[i]] ? (tCount[t[i]] += 1) : (tCount[t[i]] = 1);
  }

  return Object.entries(sCount).every(([key, value]) => tCount[key] === value);
};
