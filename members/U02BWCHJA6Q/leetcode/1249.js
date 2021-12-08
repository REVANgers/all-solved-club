/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function (s) {
  const deleteLeft = [];
  const deleteRight = [];

  for (let i = 0; i < s.length; i++) {
    const c = s[i];

    if (c === '(') {
      deleteLeft.push(i);

      continue;
    }

    if (c === ')') {
      if (deleteLeft.length > 0) {
        deleteLeft.shift();

        continue;
      }

      deleteRight.push(i);

      continue;
    }
  }

  return [...s]
    .filter(
      (_, index) => !deleteLeft.includes(index) && !deleteRight.includes(index),
    )
    .join('');
};
