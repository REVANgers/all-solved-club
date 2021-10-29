/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function (nums1, m, nums2, n) {
  let count = nums1.length - m;

  for (let i = 0; i < count; i++) {
    nums1.pop();
  }

  count = n;

  for (let i = 0; i < count; i++) {
    nums1.push(nums2.pop());
  }

  return nums1.sort((a, b) => a - b);
};
