/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function (nums, k) {
  let start = 0;
  let product = 1;
  let count = 0;

  for (let end = 0; end < nums.length; end++) {
    product *= nums[end];

    while (product >= k && start <= end) {
      product /= nums[start++];
    }
    count += end - start + 1;
  }

  return count;
};
