/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
  if (!p || p.length === 0) {
    return s.length === 0 ? true : false;
  }

  const matchedFirst = s.length && (p[0] === s[0] || p[0] === '.');

  if (p.length > 1 && p[1] === '*') {
    const noUseStar = isMatch(s, p.slice(2));
    const matchedByStar = matchedFirst && isMatch(s.slice(1), p);

    return noUseStar || matchedByStar;
  }

  return matchedFirst && isMatch(s.slice(1), p.slice(1));
};
