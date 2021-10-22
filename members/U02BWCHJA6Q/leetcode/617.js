/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */

var mergeTrees = function (root1, root2) {
  if (!root1 && !root2) {
    return null;
  }

  let mergedValue = 0;

  if (root1 && root1.val) {
    mergedValue += root1.val;
  }

  if (root2 && root2.val) {
    mergedValue += root2.val;
  }

  const root1Left = root1 ? root1.left : null;
  const root2Left = root2 ? root2.left : null;
  const root1Right = root1 ? root1.right : null;
  const root2Right = root2 ? root2.right : null;

  const mergedLeft = mergeTrees(root1Left, root2Left);
  const mergedRight = mergeTrees(root1Right, root2Right);

  return new TreeNode(mergedValue, mergedLeft, mergedRight);
};
