# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from idlelib.tree import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if root is None:
                return None

            left = helper(root.left)
            right = helper(root.right)

            root.left = right
            root.right = left

            return root

        return helper(root)
