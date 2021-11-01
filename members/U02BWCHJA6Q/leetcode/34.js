/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
  const first = nums.indexOf(target);

  if (first === -1) {
    return [-1, -1];
  }

  let last = first;

  for (let i = last; i < nums.length; i++) {
    last = i;
    if (nums[last] !== target) {
      last--;
      break;
    }
  }

  return [first, last];
};
