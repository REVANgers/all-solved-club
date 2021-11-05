/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  const output = [];
  let startY = 0;
  let startX = 0;
  let endY = matrix.length - 1;
  let endX = matrix[0].length - 1;

  while (startY <= endY && startX <= endX) {
    for (let x = startX; x <= endX; x++) {
      output.push(matrix[startY][x]);
    }

    for (let y = startY + 1; y <= endY; y++) {
      output.push(matrix[y][endX]);
    }

    if (startX < endX && startY < endY) {
      for (let x = endX - 1; x > startX; x--) {
        output.push(matrix[endY][x]);
      }

      for (let y = endY; y > startY; y--) {
        output.push(matrix[y][startX]);
      }
    }

    startX++;
    startY++;
    endX--;
    endY--;
  }

  return output;
};
