/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function (s) {
  const answer = [];
  let start = 0;
  let pivot = 0;

  while (pivot < s.length) {
    let last = s.lastIndexOf(s[pivot++]);
    while (pivot <= last) {
      last = Math.max(last, s.lastIndexOf(s[pivot++]));
    }
    answer.push(last - start + 1);
    start = pivot;
  }

  return answer;
};
