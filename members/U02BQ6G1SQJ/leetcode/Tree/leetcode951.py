import collections;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(curNode : Optional[TreeNode], nodeDict : collections.defaultdict) -> None:
    if (curNode.left):
        nodeDict[curNode.val].add(curNode.left.val);
        dfs(curNode.left, nodeDict);
        
    if (curNode.right):
        nodeDict[curNode.val].add(curNode.right.val);
        dfs(curNode.right, nodeDict);
        
    return None;

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        (nodeDict1, nodeDict2) = (collections.defaultdict(set), collections.defaultdict(set));
        
        if (root1):
            nodeDict1[-1].add(root1.val);
            dfs(root1, nodeDict1);
            
        if (root2):
            nodeDict2[-1].add(root2.val);
            dfs(root2, nodeDict2);
        
        # print(nodeDict1);
        # print(nodeDict2);
        
        return (nodeDict1 == nodeDict2);
