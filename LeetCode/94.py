# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        final = []
        if not root:
            return final
        return self.inorderRecursive(root, final)
    
    def inorderRecursive(self, root, final):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.inorderRecursive(root.left, final)
        final.append(root.val)
        self.inorderRecursive(root.right, final)
        return final
        