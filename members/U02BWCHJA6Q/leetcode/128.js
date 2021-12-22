/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length === 0) {
    return 0;
  }

  let max = 1;
  const set = new Set(nums);

  for (let num of nums) {
    let count = 1;
    if (set.has(num - 1)) {
      continue;
    }

    while (set.has(++num)) {
      count++;
    }

    max = Math.max(max, count);
  }

  return max;
};
