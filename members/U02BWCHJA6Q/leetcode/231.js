/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function (n) {
  if (n === 1) {
    return true;
  }

  return (
    n
      .toString(2)
      .split('')
      .reduce((acc, cur) => Number(acc) + Number(cur)) === 1
  );
};
