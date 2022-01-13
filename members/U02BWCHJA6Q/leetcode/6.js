/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  const rows = [];
  let pivot = 0;
  let row = 0;
  let upper = true;

  if (numRows === 1) {
    return s;
  }

  for (let i = 0; i < numRows; i++) {
    rows.push('');
  }

  while (pivot < s.length) {
    rows[row] += s[pivot++];

    if (row === rows.length - 1) {
      row--;
      upper = false;

      continue;
    }

    if (row === 0 && !upper) {
      row++;
      upper = true;

      continue;
    }

    if (upper) {
      row++;
    } else {
      row--;
    }
  }

  return rows.join('');
};
