class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        temp = root
        while temp.val != val:
            if temp.val > val:
                if not temp.left: temp.left = TreeNode(val)
                temp = temp.left
            else:
                if not temp.right: temp.right = TreeNode(val)
                temp = temp.right
        return root
		