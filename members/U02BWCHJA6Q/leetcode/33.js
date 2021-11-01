/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let left = 0,
    right = nums.length - 1;
  const last = nums[nums.length - 1];

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (nums[mid] === target) {
      return mid;
    }

    const isRightPosition =
      (nums[mid] <= last && target <= last) ||
      (nums[mid] > last && target > last);
    if (nums[mid] > target) {
      isRightPosition ? (right = mid - 1) : (left = mid + 1);
    } else if (nums[mid] < target) {
      isRightPosition ? (left = mid + 1) : (right = mid - 1);
    }
  }
  return -1;
};
