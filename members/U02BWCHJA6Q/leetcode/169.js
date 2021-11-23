/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  const map = new Map();
  const max = (nums.length / 2) | 0;
  let answer = 0;

  nums.some(number => {
    map.has(number) ? map.set(number, map.get(number) + 1) : map.set(number, 1);

    if (map.get(number) > max) {
      answer = number;
      return true;
    }
  });

  return answer;
};
