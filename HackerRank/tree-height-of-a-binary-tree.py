def height(root):
    if not root:
        return -1
    left = height(root.left)
    right = height(root.right)
    return left+1 if left > right else right+1
