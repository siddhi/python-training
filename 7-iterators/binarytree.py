class BinaryTreeInorderIterator:
    def __init__(self, root):
        self.stack = []
        self.node = root

    def __next__(self):
        try:
            while self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            top = self.stack.pop()
            val = top.value
            if top.right:
                self.node = top.right
            return val
        except IndexError:
            raise StopIteration


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def _add(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left._add(value)
        if value >= self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right._add(value)

    def __add__(self, values):
        for value in values:
            self._add(value)
        return self

    def __iter__(self):
        return BinaryTreeInorderIterator(self)

    def __contains__(self, value):
        if self.value == value:
            return True
        if self.left and value in self.left:
            return True
        if self.right and value in self.right:
            return True
        return False


if __name__ == "__main__":
    root = Node(10)
    root = root + [21, 101, 2, -1]
    root += [6, 3, 1, 5, 7, 12, 4, 17, 2]
    for val in root:
        print(val)
