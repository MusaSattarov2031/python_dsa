class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left_child = left
        self.right_child = right

class BinaryTree():
    def __init__(self, head = None):
        self.head = head

    def __len__(self):
        return self._get_size(self.head)

    def _get_size(self, curr):
        if curr is None:
            return 0
        
        return 1+self._get_size(curr.right_child) + self._get_size(curr.left_child)

    def __str__(self):
        pass
    
    def add_node(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            self._add_recursive(self.head, value)
    
    def _add_recursive(self, curr, value):
        if value < curr.value:
            if curr.left_child:
                self._add_recursive(curr.left_child, value)
            else:
                curr.left_child = Node(value)
        elif value > curr.value:
            if curr.right_child:
                self._add_recursive(curr.right_child, value)
            else:
                curr.right_child = Node(value)


    def clear(self):
        self.head = None

