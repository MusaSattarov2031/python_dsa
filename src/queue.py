class Queue:
    """FIFO data structure: First in First out"""
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def __str__(self):
        res = "Start"
        for item in self._data:
            res += f"->{item}"
        res+="->End"
        return res

    def enqueue(self, item):
        self._data.insert(0, item)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def deque(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        else:
            res = self._data.pop()
            return res
        
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[-1]
    
    
    
    
