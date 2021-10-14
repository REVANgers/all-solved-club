/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
  let result = [];
  let i = a.length - 1;
  let j = b.length - 1;
  let carry = 0;

  while (i >= 0 || j >= 0) {
    let sum = carry;
    if (i >= 0) {
      sum += Number(a[i--]);
    }
    if (j >= 0) {
      sum += Number(b[j--]);
    }
    result.push(sum % 2);
    carry = Math.floor(sum / 2);
  }

  if (carry > 0) {
    result.push(carry);
  }

  return result.reverse().join('');
};
