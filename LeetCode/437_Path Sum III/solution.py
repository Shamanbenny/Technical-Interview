# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix = {0 : 1}
        def getPath(curr: TreeNode, currSum: int):
            if not curr:
                return 0
            else:
                currSum += curr.val
                result = prefix.get(currSum - targetSum, 0)
                prefix[currSum] = prefix.get(currSum, 0) + 1
                result += getPath(curr.left, currSum)
                result += getPath(curr.right, currSum)
                prefix[currSum] -= 1
                return result
        return getPath(root, 0)
