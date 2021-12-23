/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
  const m = matrix.length;
  const n = matrix[0].length;

  for (let y = 0; y < m; y++) {
    for (let x = 0; x < n; x++) {
      if (matrix[y][x] === 0) {
        matrix[y][x] = 'Z';
      }
    }
  }

  for (let y = 0; y < m; y++) {
    for (let x = 0; x < n; x++) {
      if (matrix[y][x] === 'Z') {
        for (let column = 0; column < n; column++) {
          if (matrix[y][column] === 'Z') {
            continue;
          }

          matrix[y][column] = 0;
        }

        for (let row = 0; row < m; row++) {
          if (matrix[row][x] === 'Z') {
            continue;
          }

          matrix[row][x] = 0;
        }
      }
    }
  }

  for (let y = 0; y < m; y++) {
    for (let x = 0; x < n; x++) {
      if (matrix[y][x] === 'Z') {
        matrix[y][x] = 0;
      }
    }
  }
};
