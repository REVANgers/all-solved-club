/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var addStrings = function (num1, num2) {
  let i = num1.length - 1;
  let j = num2.length - 1;
  let carry = 0;
  let answer = [];

  while (i >= 0 || j >= 0) {
    let sum = carry;

    if (i >= 0) {
      sum += Number(num1[i--]);
    }
    if (j >= 0) {
      sum += Number(num2[j--]);
    }

    if (sum >= 10) {
      carry = 1;
      sum = sum % 10;
    } else {
      carry = 0;
    }

    answer.push(sum);
  }

  if (carry > 0) {
    answer.push(carry);
  }

  return answer.reverse().join('');
};
