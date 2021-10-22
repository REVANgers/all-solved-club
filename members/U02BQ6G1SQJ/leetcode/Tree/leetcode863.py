import collections;

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(curNode : TreeNode, adjDict : dict) -> None:
    if (curNode.left):
        adjDict[curNode].append(curNode.left);
        adjDict[curNode.left].append(curNode);
        dfs(curNode.left, adjDict);
        
    if (curNode.right):
        adjDict[curNode].append(curNode.right);
        adjDict[curNode.right].append(curNode);
        dfs(curNode.right, adjDict);
        
    return None;

def bfs(startNode : TreeNode, targetDist : int, adjDict : dict) -> list:
    (answerList, dq, visitSet) = ([], collections.deque([[startNode, 0]]), set([startNode]));
    
    while (dq):
        (curNode, curDist) = dq.popleft();
        
        # print(curNode.val, curDist);
        
        if (curDist == targetDist):
            answerList.append(curNode.val);
        elif (curDist > targetDist):
            break;
            
        for nextNode in adjDict[curNode]:
            if (nextNode in visitSet):
                continue;
                
            visitSet.add(nextNode);
            dq.append([nextNode, curDist + 1]);
            
    return answerList;

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjDict = collections.defaultdict(list);
        
        dfs(root, adjDict);
        
        # print(adjDict);
        
        return bfs(target, k, adjDict);
