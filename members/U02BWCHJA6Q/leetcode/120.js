/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function (triangle) {
  const dp = [];
  triangle.forEach(a => dp.push(Array(a.length).fill(0)));
  dp[0][0] = triangle[0][0];

  for (let i = 1; i < dp.length; i++) {
    for (let j = 0; j < dp[i].length; j++) {
      let a = Infinity;
      let b = Infinity;
      if (j - 1 >= 0) {
        a = dp[i - 1][j - 1] + triangle[i][j];
      }
      if (j <= i - 1) {
        b = dp[i - 1][j] + triangle[i][j];
      }

      dp[i][j] = Math.min(a, b);
    }
  }

  return Math.min(...dp[dp.length - 1]);
};
