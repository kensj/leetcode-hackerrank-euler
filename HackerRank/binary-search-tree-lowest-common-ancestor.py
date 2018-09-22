def lca(root, v1, v2):
    found = valExists(root, v1) or valExists(root, v2)
    return root if found else lca(root.left, v1, v2) or lca(root.right, v1, v2)

def valExists(root, val):
    if not root:
        return False
    if root.info == val:
        return True
    left = valExists(root.left, val)
    right = valExists(root.right, val)
    return left or right
	