def levelOrder(root):
    queue = []
    queue.append(root)
    while len(queue):
        node = queue.pop(0)
        print(node.info, end=' ')
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
