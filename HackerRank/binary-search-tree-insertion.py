    def insert(self, val):
        if not self.root or type(self.root) is 'NoneType': self.root = Node(val)
        else: self.root = self.insertNode(self.root, val)
        return self
    def insertNode(self, root, val):
        if not root: root = Node(val)
        elif val < root.info: root.left = self.insertNode(root.left, val)
        elif val > root.info: root.right = self.insertNode(root.right, val)
        return root
