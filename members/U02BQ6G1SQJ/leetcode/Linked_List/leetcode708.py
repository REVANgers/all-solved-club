import math;

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if (not head):
            insertNode = Node(insertVal, None);
            insertNode.next = insertNode;
            return insertNode;
        
        (minNode, maxNode, targetNode, curNode) = (head, head, (head if (insertVal > head.val) else Node(-math.inf, None)), head.next);
        
        while (curNode != head):
            if (minNode.val >= curNode.val):
                minNode = curNode;
                
            if (maxNode.val <= curNode.val):
                maxNode = curNode;
                
            if ((targetNode.val <= curNode.val) and (insertVal >= curNode.val)):
                targetNode = curNode;
                
            curNode = curNode.next;
            
        # print("min :", minNode.val);
        # print("max :", maxNode.val);
        # print("target :", targetNode.val);
        # print("cur :", curNode.val);
        # print();
        
        if ((targetNode.val == -math.inf) or (minNode.val >= insertVal) or (maxNode.val <= insertVal)):
            # print("CASE 1");
            
            insertNode = Node(insertVal, maxNode.next);
            maxNode.next = insertNode;
        else:
            # print("CASE 2");
            
            insertNode = Node(insertVal, targetNode.next);
            targetNode.next = insertNode;
        
        return head;
