#node.py

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def is_leaf(self):
        return not (self.left or self.right)

    def get_children(self):
        return list(filter(lambda x: x, [self.left, self.right]))
