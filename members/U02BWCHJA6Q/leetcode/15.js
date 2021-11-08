/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const triple = [];

  if (nums.length < 3) {
    return triple;
  }

  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i - 1] === nums[i]) {
      continue;
    }

    const one = nums[i];

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      let two = nums[left];
      let three = nums[right];
      const sum = one + two + three;

      if (sum === 0) {
        triple.push([one, two, three]);

        while (nums[left] === nums[left + 1]) {
          left++;
        }
        while (nums[right] === nums[right - 1]) {
          right--;
        }

        left++;
        right--;

        continue;
      }

      if (sum > 0) {
        right--;

        continue;
      }

      if (sum < 0) {
        left++;

        continue;
      }
    }
  }

  return triple;
};
