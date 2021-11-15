# reference : https://leetcode.com/problems/find-duplicate-subtrees/discuss/106020/Python-easy-understand-solution

import collections;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
def dfs(curNode : Optional[TreeNode], leftDict : collections.defaultdict, rightDict : collections.defaultdict) -> None:
    if (curNode.left):
        leftDict[curNode.val][curNode.left.val] += 1;
        dfs(curNode.left, leftDict, rightDict);
        
    if (curNode.right):
        rightDict[curNode.val][curNode.right.val] += 1;
        dfs(curNode.right, leftDict, rightDict);
    
    return None;
"""

def dfs(curNode : Optional[TreeNode], nodeDict : collections.defaultdict(list)) -> str:
    if (not curNode):
        return "null";
    
    key = "%s_%s_%s" % (str(curNode.val), dfs(curNode.left, nodeDict), dfs(curNode.right, nodeDict));
    nodeDict[key].append(curNode);
    return key;

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        if (not root):
            return None;
        
        (leftDict, rightDict) = (collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter));
        
        dfs(root, leftDict, rightDict);
        
        # print(leftDict);
        # print(rightDict);
        """
    
        nodeDict = collections.defaultdict(list);
        dfs(root, nodeDict);
        
        # print(nodeDict);
        
        return [nodeDict[k][0] for k in nodeDict.keys() if (len(nodeDict[k]) > 1)];
