/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function (numRows) {
  const output = [[1]];

  for (let i = 1; i < numRows; i++) {
    const row = [];
    for (let j = 0; j <= i; j++) {
      if (j === 0 || j === i) {
        row.push(1);

        continue;
      }

      row.push(output[i - 1][j - 1] + output[i - 1][j]);
    }
    output.push(row);
  }

  return output;
};
