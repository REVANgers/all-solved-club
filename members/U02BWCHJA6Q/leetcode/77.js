/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function (n, k) {
  const array = [];

  for (let i = 1; i <= n; i++) {
    array.push(i);
  }

  return getCombinations(array, k);
};

const getCombinations = (array, number) => {
  const result = [];

  if (number === 1) {
    return array.map(v => [v]);
  }

  array.forEach((fixed, index) => {
    const rest = array.slice(index + 1);
    const restCombinations = getCombinations(rest, number - 1);
    const combined = restCombinations.map(v => [fixed, ...v]);

    result.push(...combined);
  });

  return result;
};
