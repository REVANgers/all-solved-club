# reference : https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/discuss/905119/Solution-in-Python

import abc 
from abc import ABC, abstractmethod 

OPERATOR_SET = set(['+', '-', '*', '/']);

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass;
    
class MyNode(ABC):
    def __init__(self, val = '', left = None, right = None):
        self.val = val;
        self.left = left;
        self.right = right;
    
    def evaluate(self) -> int:
        result = self.val;
        
        if (self.val == '+'):
            result = self.left.evaluate() + self.right.evaluate();
        elif (self.val == '-'):
            result = self.left.evaluate() - self.right.evaluate();
        elif (self.val == '*'):
            result = self.left.evaluate() * self.right.evaluate();
        elif (self.val == '/'):
            result = self.left.evaluate() // self.right.evaluate();
            
        return int(result);

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = [];
        
        for curCh in postfix:
            if curCh in OPERATOR_SET:
                (right, left) = (stack.pop(), stack.pop());
                stack.append(MyNode(curCh, left, right));
            else:
                stack.append(MyNode(curCh, None, None));
                
        return stack[0];
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
