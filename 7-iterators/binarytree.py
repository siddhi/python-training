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

    def add(self, values):
        for value in values:
            self._add(value)
        return self


if __name__ == "__main__":
    root = Node(10)
    root.add([21, 101, 2, -1])
    root.add([6, 3, 1, 5, 7, 12, 4, 17, 2])
    print(root.left.value)
