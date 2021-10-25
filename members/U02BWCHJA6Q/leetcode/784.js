/**
 * @param {string} s
 * @return {string[]}
 */
var letterCasePermutation = function (s) {
  const output = [];
  const helper = (string, index, result) => {
    if (index === string.length) {
      output.push(result.join(''));

      return;
    }

    if (isNaN(string[index])) {
      helper(string, index + 1, [...result, string.toLowerCase()[index]]);
      helper(string, index + 1, [...result, string.toUpperCase()[index]]);
    } else {
      helper(string, index + 1, [...result, string[index]]);
    }
  };

  helper(s, 0, []);

  return output;
};
