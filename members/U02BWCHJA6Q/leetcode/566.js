/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function (mat, r, c) {
  if (mat.length * mat[0].length !== r * c) {
    return mat;
  }

  const output = [];
  let index = 0;

  mat = mat.flat();

  for (let y = 0; y < r; y++) {
    const row = [];
    for (let x = 0; x < c; x++) {
      row.push(mat[index++]);
    }
    output.push(row);
  }

  return output;
};
