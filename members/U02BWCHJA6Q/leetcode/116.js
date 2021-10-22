/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */

/**
 * @param {Node} root
 * @return {Node}
 */

const changeNext = root => {
  if (!root || !root.left || !root.right) {
    return;
  }

  let left = root.left;
  let right = root.right;
  left.next = right;

  if (root.next) {
    right.next = root.next.left;
  }

  changeNext(left);
  changeNext(right);
};

var connect = function (root) {
  if (!root) {
    return root;
  }

  changeNext(root);

  return root;
};
