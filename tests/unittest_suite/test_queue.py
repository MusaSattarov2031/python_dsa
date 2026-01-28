import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        return super().setUp()
    
    def test_enqueue(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.q.enqueue(30)

        self.assertEqual(len(self.q), 3)

    def test_is_empty(self):
        self.assertTrue(self.q.is_empty())
        self.q.enqueue(10)
        self.assertFalse(self.q.is_empty())

    def test_deque(self):
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.q.enqueue(30)

        res10 = self.q.deque()
        res20 = self.q.deque()
        res30 = self.q.deque()

        self.assertEqual(res10, 10)
        self.assertEqual(res20, 20)
        self.assertEqual(res30, 30)

        self.assertEqual(len(self.q), 0)

        with self.assertRaises(IndexError):
            self.q.deque()

    def test_str(self):
        self.assertEqual(str(self.q), "Start->End")
        self.q.enqueue(10)
        self.q.enqueue(20)
        self.q.enqueue(30)
        self.assertEqual(str(self.q), "Start->30->20->10->End")
    
    def test_front(self):
        self.q.enqueue(10)
        self.assertEqual(self.q.front(), 10)
        self.q.enqueue(20)
        self.assertEqual(self.q.front(), 10)
        self.q.deque()
        self.q.deque()

        with self.assertRaises(IndexError):
            self.q.front()