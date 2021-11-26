/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  let y = 0;
  let x = matrix[0].length - 1;

  while (x >= 0 && y < matrix.length) {
    if (matrix[y][x] === target) {
      return true;
    }

    if (matrix[y][x] > target) {
      x--;
    } else {
      y++;
    }
  }

  return false;
};
