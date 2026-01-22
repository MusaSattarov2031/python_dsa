class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if not self._isValidIndex(index):
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value
    
    def __setitem__(self, index, value):
        if not self._isValidIndex(index):
            raise IndexError("Index out of range")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.value = value
    
    def __str__(self):
        res = ""
        curr = self.head
        while curr != None:
            res += f"{curr.value}->"
            curr = curr.next
        res += "None"
        return res

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.size += 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(value)
        self.size += 1
    
    def prepend(self, value):
        if self.head == None:
            self.head = Node(value)
            self.size += 1
            return
        new_head = Node(value, self.head)
        self.head = new_head
        self.size += 1


    def _isValidIndex(self, index):
        if index<0 or index>=self.size:
            return False
        return True
    
    def insert_at(self, value, index):
        self.size +=1
        if index == 0:
            self.prepend(value)
            return
        if self._isValidIndex(index):
            curr = self.head
            for i in range(0, index-1):
                curr = curr.next
            temp = curr.next
            new_node = Node(value, temp)
            curr.next = new_node
        else:
            self.size -= 1
            raise IndexError
    
    def pop(self):
        curr = self.head()
        while curr.next.next != None:
            curr = curr.next
        res = curr.next.value
        curr.next = None
        self.size -= 1
        return res
    
    def remove(self, value):
        curr = self.head()
        while curr.next != None:
            if curr.next.value == value:
                curr.next = curr.next.next
                self.size -= 1
                return
            else:
                curr = curr.next
    
    def delete_at(self, index):
        if self._isValidIndex(index):
            if index == 0:
                self.head = self.head.next
            else:
                prev = self.head
                to_delete = prev.next
                for i in range(0, index-1):
                    prev = to_delete
                    to_delete = prev.next
                prev.next = to_delete.next
            self.size -= 1
        else:
            raise IndexError
    
    def search(self, value):
        curr = self.head
        while curr != None:
            if curr.value == value:
                return True
        return False
    
    def index_of(self, value):
        curr = self.head
        ind = 0
        while curr != None:
            if curr.value == value:
                return ind
            else:
                ind +=1
                curr = curr.next
        return -1
    
    def is_empty(self):
        if len(self) == 0:
            return True
        else:
            return False
        
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        res = LinkedList()
        res.head = prev
        res.size = self.size
        self = res
    
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
