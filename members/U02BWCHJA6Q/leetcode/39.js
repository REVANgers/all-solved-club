/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
  const answer = [];
  candidates = candidates
    .filter(number => number <= target)
    .sort((a, b) => a - b);

  const dfs = (pivot, sum, array) => {
    if (sum === target) {
      answer.push(array);

      return;
    }

    if (pivot === candidates.length || sum + candidates[pivot] > target) {
      return;
    }

    dfs(pivot + 1, sum, [...array]);
    dfs(pivot, sum + candidates[pivot], [...array, candidates[pivot]]);
  };

  dfs(0, 0, []);

  return answer;
};
