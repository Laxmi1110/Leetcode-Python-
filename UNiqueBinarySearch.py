# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int):
        
        def solve(start, end):
            
            if start > end:
                return [None]
            
            ans = []
            
            for i in range(start, end + 1):
                
                leftSubtree = solve(start, i - 1)
                rightSubtree = solve(i + 1, end)
                
                for left in leftSubtree:
                    for right in rightSubtree:
                        
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        
                        ans.append(root)
            
            return ans
        
        return solve(1, n)
