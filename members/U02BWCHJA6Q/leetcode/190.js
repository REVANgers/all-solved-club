/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  const string = n.toString(2);
  let binary = '';

  for (let i = 0; i < 32 - string.length; i++) {
    binary += '0';
  }
  binary += string;

  return parseInt(binary.split('').reverse().join(''), 2);
};
