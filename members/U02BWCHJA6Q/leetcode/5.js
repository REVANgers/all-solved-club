/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  let max = s.length;

  const isPalindrom = (start, end) => {
    while (start <= end) {
      if (s[start++] !== s[end--]) {
        return false;
      }
    }

    return true;
  };

  for (let length = max; length >= 2; length--) {
    for (let j = 0; j <= max - length; j++) {
      if (isPalindrom(j, j + length - 1)) {
        return s.slice(j, j + length);
      }
    }
  }

  return s[0];
};
