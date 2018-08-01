class BinaryTreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def add(self, number):
        if number > self.val:
            if self.right:
                self.right.add(number)
            else:
                self.right = BinaryTreeNode(number)
        else:
            if self.left:
                self.left.add(number)
            else:
                self.left = BinaryTreeNode(number)

    def inorder(self):
        pass

root = BinaryTreeNode(10)
root.add(4)
root.add(6)
root.add(5)
root.add(25)
root.add(100)
root.inorder()
