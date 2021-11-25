/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function (rowIndex) {
  if (rowIndex === 0) {
    return [1];
  }

  let row = [1, 1];

  for (let i = 2; i <= rowIndex; i++) {
    const nextRow = [1];

    for (let j = 1; j < i; j++) {
      nextRow.push(row[j - 1] + row[j]);
    }
    nextRow.push(1);

    row = nextRow;
  }

  return row;
};
