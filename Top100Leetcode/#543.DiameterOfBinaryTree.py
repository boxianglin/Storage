# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.d = 0;
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.d = max(left+right,self.d) #keep track of left+right depth for the cur node
            return max(left, right) + 1 #each lavel back adds depth 1
        dfs(root)
        return self.d

# Theoretically a single node depth is 0
class Solution1:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.d = 0;
        def dfs(root):
            if not root: return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.d = max(left+right+2,self.d)
            return max(left, right) + 1
        dfs(root)
        return self.d
