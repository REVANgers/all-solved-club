/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  let left = 0;
  let right = nums.length - 1;

  if (nums.length === 1) {
    return 0;
  }

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    console.log(
      mid,
      mid - 1 < 0 || nums[mid - 1] < nums[mid],
      mid + 1 >= nums.length || nums[mid + 1] < nums[mid],
      nums[mid],
    );

    if (
      (mid - 1 < 0 || nums[mid - 1] < nums[mid]) &&
      (mid + 1 >= nums.length || nums[mid + 1] < nums[mid])
    ) {
      return mid;
    }

    if (mid === 0 || nums[mid - 1] <= nums[mid]) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
};
