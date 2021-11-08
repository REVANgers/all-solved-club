import collections;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(curNode : Optional[TreeNode], nodeDict : collections.defaultdict(list), curLevel : int) -> None:
    if (not curNode):
        return None;
    
    nodeDict[curLevel].append(curNode.val);
    dfs(curNode.left, nodeDict, curLevel + 1);
    dfs(curNode.right, nodeDict, curLevel + 1);
    return None;

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodeDict = collections.defaultdict(list);
        
        dfs(root, nodeDict, 0);
        
        # print(nodeDict);
        
        return [(nodeDict[k] if (k % 2 == 0) else nodeDict[k][ : : -1]) for k in sorted(nodeDict.keys())];
