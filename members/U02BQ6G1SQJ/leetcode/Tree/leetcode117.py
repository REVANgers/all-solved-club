import collections;

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

def dfs(curNode : 'Node', levelDict : collections.defaultdict, curLevel : int) -> None:
    if (not curNode):
        return None;
    
    levelDict[curLevel].append(curNode);
    dfs(curNode.left, levelDict, curLevel + 1);
    dfs(curNode.right, levelDict, curLevel + 1);
    return None;

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        levelDict = collections.defaultdict(list);
        
        dfs(root, levelDict, 0);
        
        # print(levelDict);
        
        for val in levelDict.values():
            for nodeIdx in range(len(val) - 1):
                val[nodeIdx].next = val[nodeIdx + 1];
                
        return root;
