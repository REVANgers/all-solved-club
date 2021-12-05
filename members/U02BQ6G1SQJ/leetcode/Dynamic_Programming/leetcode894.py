# reference : https://leetcode.com/problems/all-possible-full-binary-trees/discuss/163429/Simple-Python-recursive-solution.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy;

def dfs(nodeCnt : int, depth : int, answerList : List[Optional[TreeNode]], root : TreeNode, curNode : TreeNode) -> None:
    if (nodeCnt == depth):
        answerList.append(copy.deepcopy(root));
        return None;
    
    (curNode.left, curNode.right) = (TreeNode(0, None, None), TreeNode(0, None, None));
    dfs(nodeCnt, depth + 2, answerList, root, curNode.left);
    dfs(nodeCnt, depth + 2, answerList, root, curNode.right);
    return None;

class Solution:
    answerDict = {0 : [], 1 : [TreeNode(0, None, None)]};
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if (n % 2 == 0):
            return None;
        
        """
        (answerList, root) = ([], TreeNode(0, None, None));
        
        dfs(n, 1, answerList, root, root);
        
        return answerList;
        """
        
        if n not in Solution.answerDict.keys():
            tmpList = [];
            
            for k in range(1, n - 1, 2):
                for left in self.allPossibleFBT(k):
                    for right in self.allPossibleFBT(n - k - 1):
                        root = TreeNode(0, left, right);
                        tmpList.append(root);
            
            Solution.answerDict[n] = tmpList;
            
        return Solution.answerDict[n];
