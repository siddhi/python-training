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
        if self.left:
            yield from self.left.inorder()
        yield self.val
        if self.right:
            yield from self.right.inorder()

class SortedList:
    def __init__(self, initial_values):
        value_iterator = iter(initial_values)
        self.tree = BinaryTreeNode(next(value_iterator))
        for val in value_iterator:
            self.tree.add(val)

    def __add__(self, other):
        new_list = SortedList(self)
        for val in other:
            new_list.tree.add(val)
        return new_list

    def __iter__(self):
        return self.tree.inorder()

lst = SortedList([100, 10, -2, 4, 7])
lst = lst + set([7, 11, 92, 5])
for item in lst:
    print(item)
