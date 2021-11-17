import collections;

MAX_NODE_CNT = 100;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(curNode : Optional[TreeNode], curR : int, curC : int, nodeDict : collections.defaultdict) -> None:
    if (not curNode):
        return None;
    
    nodeDict[tuple([curR, curC])].append(curNode.val);
    dfs(curNode.left, curR + 1, curC - 1, nodeDict);
    dfs(curNode.right, curR + 1, curC + 1, nodeDict);
    return None;

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        (answerList, curC, nodeDict) = ([], -MAX_NODE_CNT, collections.defaultdict(list));
        
        dfs(root, 0, 0, nodeDict);
        
        # print(nodeDict);
        
        for curPos in sorted(nodeDict.keys(), key = lambda k : (k[1], k[0])):
            (r, c) = curPos;
        
            # print(r, c, nodeDict[curPos]);
            
            if (curC == c):
                answerList[-1] += nodeDict[curPos];
            else:
                answerList.append(nodeDict[curPos]);
                curC = c;
                
        return answerList;
