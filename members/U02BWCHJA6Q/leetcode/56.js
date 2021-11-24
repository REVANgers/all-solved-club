/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
  intervals.sort((a, b) => a[0] - b[0]);

  const merged = [];
  let before = intervals.shift();

  while (intervals.length > 0) {
    const next = intervals.shift();
    let merge = null;

    if (Math.max(before[0], next[0]) <= Math.min(before[1], next[1])) {
      merge = [Math.min(before[0], next[0]), Math.max(before[1], next[1])];
      before = merge;
    } else {
      merged.push(before);
      before = next;
    }
  }

  merged.push(before);

  return merged;
};
