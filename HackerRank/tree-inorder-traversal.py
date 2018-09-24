def inOrder(root):
    if not root: return
    inOrder(root.left)
    print(root.info, end=' ')
    inOrder(root.right)
