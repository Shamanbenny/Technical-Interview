# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def getLeaf(curr: TreeNode) -> List[int]:
            if not curr.left and not curr.right: 
                # curr is leaf node
                return [curr.val]
            # Either left and/or right node exist
            res = []
            if curr.left:
                res.extend(getLeaf(curr.left))
            if curr.right:
                res.extend(getLeaf(curr.right))
            return res

        return getLeaf(root1) == getLeaf(root2)
