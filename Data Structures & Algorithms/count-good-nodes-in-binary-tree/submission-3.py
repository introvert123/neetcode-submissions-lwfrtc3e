# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0
        self.count = 0

        def dfs(curr,maxNum):
            if not curr:
                return
                
            
            if curr.val >= maxNum:
                self.count += 1
            dfs(curr.left,max(maxNum,curr.val))
            dfs(curr.right, max(maxNum,curr.val))


        dfs(root,root.val)
        return self.count