/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let max = nums[0];
  let sub = nums[0];

  for (let i = 1; i < nums.length; i++) {
    sub = Math.max(sub + nums[i], nums[i]);
    max = Math.max(max, sub);
  }

  return max;
};
