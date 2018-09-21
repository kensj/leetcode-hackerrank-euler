# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxDepthRec(root, 0, []))
        
        
    def maxDepthRec(self, root, depth, maxd):
        if root is None:
            return [0]
        if root:
            self.maxDepthRec(root.left, depth+1, maxd)
            self.maxDepthRec(root.right, depth+1, maxd)
        maxd.append(depth+1)
        return maxd