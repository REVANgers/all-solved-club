/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
  let count = 0;
  const binary = n.toString(2);

  for (let i = 0; i < binary.length; i++) {
    if (binary[i] === '1') {
      count++;
    }
  }

  return count;
};
