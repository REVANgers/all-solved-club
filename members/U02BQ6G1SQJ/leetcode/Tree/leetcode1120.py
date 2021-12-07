# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(curNode : TreeNode, avgList : List[int]) -> List[int]:
    if (not curNode):
        return [0, 0];
    
    (leftSum, leftCnt) = dfs(curNode.left, avgList);
    (rightSum, rightCnt) = dfs(curNode.right, avgList);
    (curSum, curCnt) = (leftSum + rightSum + curNode.val, leftCnt + rightCnt + 1);
    avgList.append(curSum / curCnt);
    return [curSum, curCnt];

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        avgList = [0.0];
        dfs(root, avgList);
        return max(avgList);
