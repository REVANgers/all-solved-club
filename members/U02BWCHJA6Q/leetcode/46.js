/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
  return getPermutations(nums, nums.length);
};

const getPermutations = (array, number) => {
  const result = [];

  if (array.length === 1) {
    return array.map(v => [v]);
  }

  array.forEach((fixed, index) => {
    const rest = [...array.slice(0, index), ...array.slice(index + 1)];
    const restPermutations = getPermutations(rest, number - 1);
    const combine = restPermutations.map(v => [fixed, ...v]);

    result.push(...combine);
  });

  return result;
};
