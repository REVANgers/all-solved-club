/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  let answer = '';
  const map = [
    [1000, 'M'],
    [900, 'CM'],
    [500, 'D'],
    [400, 'CD'],
    [100, 'C'],
    [90, 'XC'],
    [50, 'L'],
    [40, 'XL'],
    [10, 'X'],
    [9, 'IX'],
    [5, 'V'],
    [4, 'IV'],
    [1, 'I'],
  ];

  for (let i = 0; i < map.length; i++) {
    const count = (num / map[i][0]) | 0;

    num = num % map[i][0];

    if (count === 0) {
      continue;
    }

    for (let j = 0; j < count; j++) {
      answer += map[i][1];
    }
  }

  return answer;
};
