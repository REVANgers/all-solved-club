/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
var intervalIntersection = function (firstList, secondList) {
  const intervals = [];

  while (firstList.length > 0 && secondList.length > 0) {
    const a = firstList[0];
    const b = secondList[0];

    let left, right;
    if (a[1] < b[1]) {
      left = firstList.shift();
      right = b;
    } else {
      left = secondList.shift();
      right = a;
    }

    if (left[1] >= right[0]) {
      intervals.push([Math.max(left[0], right[0]), left[1]]);
    }
  }

  return intervals;
};
