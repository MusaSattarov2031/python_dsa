from linked_list import LinkedList

class Stack:
    """
    A LIFO (Last-In, First-Out) data structure implemented using a LinkedList.

    Elements are added to and removed from the 'top' of the stack.
    """
    def __init__(self):
        self._data = LinkedList()
    
    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        res = ""
        curr = self._data.head
        while curr:
            res+=f"{curr.value}->"
        res+="Top"
        return res
    
    def push(self, value):
        """adds element in the end of stack"""
        self._data.prepend(value)


    def pop(self):
        """deletes and returns  the last element"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.delete_at(0)


    def peek(self):
        """returns last element's value without erasing it"""
        if self.is_empty():
            raise IndexError("peek of empty stack")
        return self._data[0]

    def is_empty(self):
        """returns True if stack is empty"""
        if len(self._data == 0):
            return True
        return False