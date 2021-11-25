/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
  const N = matrix.length;
  const copied = matrix.map(v => [...v]);

  for (let y = 0; y < N; y++) {
    for (let x = 0; x < N; x++) {
      const source = copied[y][x];
      matrix[x][N - 1 - y] = source;
    }
  }
};
