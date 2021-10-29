# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def deleteNode(curVal : int, curNode : TreeNode, parentNode : TreeNode, addSet : set, removeSet : set) -> None:
    if (curVal == curNode.val):
        if (curNode.left):
            addSet.add(curNode.left);
            
        if (curNode.right):
            addSet.add(curNode.right);

        if (parentNode):
            if (curNode == parentNode.left):
                parentNode.left = None;
            elif (curNode == parentNode.right):
                parentNode.right = None;
        else:
            removeSet.add(curNode);
            
        return None;
    
    if (curNode.left):
        deleteNode(curVal, curNode.left, curNode, addSet, removeSet);
        
    if (curNode.right):
        deleteNode(curVal, curNode.right, curNode, addSet, removeSet);
        
    return None;

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        rootSet = set([root]);
        
        for curVal in to_delete:
            (addSet, removeSet) = (set(), set())
            
            for curRoot in rootSet:
                deleteNode(curVal, curRoot, None, addSet, removeSet);
                
            rootSet = ((rootSet | addSet) - removeSet);
                
        return rootSet;
