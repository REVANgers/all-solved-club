class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        tree = ['root']
        for node in preorder.split(','):
            print(tree)
            if tree:
                tree.pop()
            else:
                return False
            if node != '#':
                tree.extend(('right', 'left'))
        return not tree
