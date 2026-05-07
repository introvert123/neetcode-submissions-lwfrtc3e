# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        #What we compute	Value
        #dfs() return	height in nodes
        #res	diameter in edges
        #diameter - longest path doesn't necessarily pass through the root
        #so at every node(with left and right), we try to find the diameter max
        def dfs(root):

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left + right) #diameter

            return 1 + max(left,right)

        dfs(root)
        return self.res
            


        