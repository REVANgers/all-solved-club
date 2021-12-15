/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function (n) {
  return Array(n)
    .fill(0)
    .map((_, index) => {
      const i = index + 1;

      if (i % 3 === 0 && i % 5 === 0) {
        return 'FizzBuzz';
      }
      if (i % 3 === 0) {
        return 'Fizz';
      }
      if (i % 5 === 0) {
        return 'Buzz';
      }
      return i.toString();
    });
};
