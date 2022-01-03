/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const set = new Set();

  nums.forEach(number => set.add(number));

  for (let i = 0; i < set.size + 1; i++) {
    if (set.has(i)) {
      continue;
    }

    return i;
  }
};
