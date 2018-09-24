def postOrder(root):
    if not root: return
    postOrder(root.left)
    postOrder(root.right)
    print(root.info, end=' ')
