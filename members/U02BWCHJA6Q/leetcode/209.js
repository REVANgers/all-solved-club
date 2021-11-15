/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
  let start = 0;
  let end = 0;
  let sum = 0;
  let min = Infinity;

  while (start <= end && end < nums.length) {
    sum += nums[end++];

    while (sum >= target) {
      min = Math.min(min, end - start);
      sum -= nums[start++];
    }
  }

  return min === Infinity ? 0 : min;
};
