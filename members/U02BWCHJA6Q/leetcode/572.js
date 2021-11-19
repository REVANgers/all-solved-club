/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  const isSame = (a, b) => {
    if (!a && !b) {
      return true;
    }
    if (!a || !b) {
      return false;
    }
    if (a.val !== b.val) {
      return false;
    }

    return isSame(a.left, b.left) && isSame(a.right, b.right);
  };

  const search = (root, target) => {
    if (!root) {
      return false;
    }

    if (root.val === target.val) {
      if (isSame(root, target)) {
        return true;
      }
    }

    if (search(root.left, target) || search(root.right, target)) {
      return true;
    }

    return false;
  };

  if (!root) {
    return false;
  }

  return search(root, subRoot);
};
