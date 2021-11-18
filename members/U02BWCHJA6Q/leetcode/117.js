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
var connect = function (root) {
  if (!root) {
    return null;
  }

  const q = [root];

  while (q.length) {
    const SIZE = q.length;
    let prev = null;

    for (let i = 0; i < SIZE; i++) {
      let node = q.shift();

      node.next = prev;
      prev = node;

      if (node.right) {
        q.push(node.right);
      }
      if (node.left) {
        q.push(node.left);
      }
    }
  }

  return root;
};
