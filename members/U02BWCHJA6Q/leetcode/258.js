/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function (num) {
  const nextNumber = num
    .toString()
    .split('')
    .reduce((acc, cur) => (acc += Number(cur)), 0);

  if (nextNumber >= 10) {
    return addDigits(nextNumber);
  }

  return nextNumber;
};
