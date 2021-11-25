/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function (n) {
  const matrix = Array.from(Array(n), () => Array(n).fill(0));

  let number = 1;

  let startY = 0;
  let startX = 0;
  let endY = n - 1;
  let endX = n - 1;

  while (startX <= endX) {
    for (let x = startX; x <= endX; x++) {
      matrix[startY][x] = number++;
    }
    for (let y = startY + 1; y < endY; y++) {
      matrix[y][endX] = number++;
    }
    for (let x = endX; x > startX; x--) {
      matrix[endY][x] = number++;
    }
    for (let y = endY; y > startY; y--) {
      matrix[y][startX] = number++;
    }
    startY++;
    endY--;
    startX++;
    endX--;
  }

  return matrix;
};
