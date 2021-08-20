# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def nodeSum(node: Optional[TreeNode]):
            if not node.left and not node.right:
                return node.val
            if node.left:
                node.val += nodeSum(node.left)
            if node.right:
                node.val += nodeSum(node.right)
            return node.val
        nodeSum(root)
        queue = [root]
        total_sum = root.val
        half_total_sum = total_sum / 2
        min_diff = 99999999
        min_diff_sum = 0
        while queue:
            node = queue.pop(0)
            diff = abs(half_total_sum - node.val)
            if diff < min_diff:
                min_diff = diff
                min_diff_sum = node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        answer = min_diff_sum * (total_sum - min_diff_sum) % 1000000007
        return answer
