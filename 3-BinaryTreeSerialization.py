# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.
# 
# For example, given the following Node class
# 
# class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#
# The following test should pass:
# 
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

#def serialize(root):


def traverse_preorder(root):
    if root == None:
        return
    
    print root.val
    traverse_preorder(root.left)
    traverse_preorder(root.right)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))
traverse_preorder(node)

# assert deserialize(serialize(node)).left.left.val == 'left.left'
