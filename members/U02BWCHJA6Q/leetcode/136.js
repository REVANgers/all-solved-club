/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  const set = new Set();

  nums.forEach(num => {
    if (set.has(num)) {
      set.delete(num);

      return;
    }

    set.add(num);
  });

  return [...set][0];
};
