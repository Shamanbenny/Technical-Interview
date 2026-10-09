# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isGood(curr: TreeNode, currMax: int) -> int:
            if not curr:
                # curr doesn't exist
                return 0
            if currMax > curr.val:
                # curr is therefore not good
                return isGood(curr.left, currMax) + isGood(curr.right, currMax)
            else:
                # curr is good (if currMax <= curr.val)
                return isGood(curr.left, curr.val) + isGood(curr.right, curr.val) + 1
        return isGood(root, root.val)
