/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
  let closest = Infinity;
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    let start = i + 1;
    let end = nums.length - 1;

    while (start < end) {
      let sum = nums[i] + nums[start] + nums[end];

      if (Math.abs(target - closest) > Math.abs(target - sum)) {
        closest = sum;

        if (sum === target) {
          break;
        }
      }

      sum > target ? end-- : start++;
    }
  }

  return closest;
};
