from src.queue import Queue

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
        
        return 1 + self._get_size(curr.right_child) + self._get_size(curr.left_child)

    def __str__(self):
        """
        Prints tree in acsended order        
        """
        res = ""
        if not self.head:
            return ""
        else:
            res += self._rec_print(self.head)
        
        return (res.strip())
    
    def _rec_print(self, curr: Node):
        res = ""
        if curr.left_child:
            res += self._rec_print(curr.left_child)
        res += f"{curr.value} "
        if curr.right_child:
            res += self._rec_print(curr.right_child)
        return res

    
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

    def delete_node(self, value):
        """
        Delete node, dont touch child nodes
        """

        self.head = self._delete_recursively(self.head, value)
    
    def _delete_recursively(self, curr, value):
        if curr:
            if curr.value > value:
                curr.left_child = self._delete_recursively(curr.left_child, value)
            elif curr.value < value:
                curr.right_child = self._delete_recursively(curr.right_child, value)
            else:
                # Case if at edge - Done
                # Case if only right exists
                # Case if only left exists 
                # case if both exists
                if curr.right_child and curr.left_child:
                    successor = self._get_min(curr.right_child)
                    curr.value = successor.value
                    curr.right_child = self._delete_recursively(curr.right_child, successor.value)
                elif curr.right_child:# Case if only right exists
                    return curr.right_child
                elif curr.left_child: # Case if only left exists
                    return curr.left_child
                else:
                    return None
        return curr
    
    def _get_min(self, node):
        while node.left_child:
            node = node.left_child
        return node
    
    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.left_child if value < curr.value else curr.right_child
        return False
    
    def get_height(self):
        return self._get_height_rec(self.head)
    
    def _get_height_rec(self, curr):
        if not curr:
            return -1
        return 1 + max(self._get_height_rec(curr.right_child),
                       self._get_height_rec(curr.left_child))
    
    def find_min(self):
        curr = self.head
        return self._get_min(curr).value
    
    def find_max(self):
        curr = self.head
        while curr.right_child:
            curr = curr.right_child

        return curr.value
    
    def as_list(self):
        results = []
        to_visit = Queue()
        if self.head:
        
            to_visit.enqueue(self.head)

            while not to_visit.is_empty():
                res = to_visit.deque()
                results.append(res.value)
                if res.left_child:
                    to_visit.enqueue(res.left_child)
                if res.right_child:
                    to_visit.enqueue(res.right_child)
        
        return results