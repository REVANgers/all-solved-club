/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
  const output = [];

  nums1.forEach(num => {
    const index = nums2.indexOf(num);

    if (index !== -1) {
      output.push(nums2.splice(index, 1));
    }
  });

  return output;
};
