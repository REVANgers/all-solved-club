/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var multiply = function (num1, num2) {
  if (num1 === '0' || num2 === '0') {
    return '0';
  }

  const result = Array(num1.length + num2.length).fill(0);

  num1 = num1
    .split('')
    .map(n => Number(n))
    .reverse();
  num2 = num2
    .split('')
    .map(n => Number(n))
    .reverse();

  for (let i = 0; i < num2.length; i++) {
    for (let j = 0; j < num1.length; j++) {
      const multiplication = num2[i] * num1[j] + result[i + j];
      result[i + j + 1] += (multiplication / 10) | 0;
      result[i + j] = multiplication % 10;
    }
  }

  if (result[result.length - 1] === 0) {
    result.pop();
  }

  return result.reverse().join('');
};
