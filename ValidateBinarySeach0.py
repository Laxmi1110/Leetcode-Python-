# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        
        def validate(node, low, high):
            if not node:
                return True

            # Current node must lie within range
            if not (low < node.val < high):
                return False

            # Check left and right subtrees
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))
