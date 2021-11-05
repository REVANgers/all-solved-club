/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];
  const map = {
    ')': '(',
    '}': '{',
    ']': '[',
  };

  for (let i = 0; i < s.length; i++) {
    const c = s[i];

    if (c === ')' || c === '}' || c === ']') {
      if (stack.length === 0) {
        return false;
      }

      if (stack.pop() !== map[c]) {
        return false;
      }

      continue;
    }

    stack.push(c);
  }

  if (stack.length > 0) {
    return false;
  }

  return true;
};
