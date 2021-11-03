/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  return nums.sort((a, b) => a - b)[0];
};
