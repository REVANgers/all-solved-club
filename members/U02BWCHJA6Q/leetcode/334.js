/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function (nums) {
  let small = Infinity;
  let middle = Infinity;

  for (const current of nums) {
    if (current <= small) {
      small = current;
    } else if (current <= middle) {
      middle = current;
    } else {
      return true;
    }
  }

  return false;
};
