/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;
  let max = 0;

  while (left < right) {
    const water = (right - left) * Math.min(height[left], height[right]);

    max = Math.max(max, water);
    height[left] < height[right] ? left++ : right--;
  }

  return max;
};
