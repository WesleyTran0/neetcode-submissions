# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root, 0)

    def maxDepthHelper(self, root: Optional[TreeNode], cur: int) -> int:
        if root is None:
            return cur

        return max(self.maxDepthHelper(root.left, cur + 1), self.maxDepthHelper(root.right, cur + 1))