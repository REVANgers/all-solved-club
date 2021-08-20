# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count = 0
        queue = [(root, -10001)]
        while queue:
            node, cur_val = queue.pop(0)
            if node.val >= cur_val:
                cur_val = node.val
                good_count += 1
            if node.left:
                queue.append((node.left, cur_val))
            if node.right:
                queue.append((node.right, cur_val))
        return good_count
