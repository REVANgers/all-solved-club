/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function (s, p) {
  const answer = [];
  const map = new Map();

  for (let i = 0; i < p.length; i++) {
    const c = p[i];

    if (map.has(c)) {
      map.set(c, map.get(c) + 1);

      continue;
    }
    map.set(c, 1);
  }

  let count = map.size;
  let right = 0;
  let left = 0;
  console.log(count);

  while (right < s.length) {
    const c = s[right];

    if (map.has(c)) {
      map.set(c, map.get(c) - 1);
    }

    if (map.get(c) === 0) {
      count--;
    }

    while (count === 0) {
      if (right - left + 1 === p.length) {
        answer.push(left);
      }
      if (map.has(s[left])) {
        map.set(s[left], map.get(s[left]) + 1);
      }
      if (map.get(s[left]) > 0) {
        count++;
      }
      left++;
    }

    right++;
  }

  return answer;
};
