/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  let negative = false;

  if (x < 0) {
    negative = true;
    x *= -1;
  }

  let reversed = Number(x.toString().split('').reverse().join(''));

  if (negative) {
    reversed *= -1;
  }

  if (reversed > Math.pow(2, 31) - 1 || reversed < Math.pow(2, 31) * -1) {
    reversed = 0;
  }

  return reversed;
};
