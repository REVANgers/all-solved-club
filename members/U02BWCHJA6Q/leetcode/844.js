/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function (s, t) {
  return backspaceString(s) === backspaceString(t);
};

const backspaceString = s => {
  const BACKSPACE = '#';
  const array = s.split('');
  const result = [];

  array.forEach((c, index) => {
    if (c === BACKSPACE) {
      if (result.length > 0) {
        result.pop();
      }
      return;
    }
    result.push(c);
  });

  return result.join('');
};
