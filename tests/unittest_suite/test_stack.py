import unittest
from src.stack import Stack
class TestStack(unittest.TestCase):
    def setUp(self):
        self.st = Stack()
        return super().setUp()
    
    def test_is_empty(self):
        self.assertTrue(self.st.is_empty())
        self.st.push(10)
        self.assertFalse(self.st.is_empty())
    
    def test_push(self):
        self.st.push(10, 20, 30)
        self.assertFalse(self.st.is_empty())
        self.assertEqual(len(self.st), 3)
        self.assertEqual(30, self.st.peek())
    
    def test_pop_on_full_stack(self):
        self.st.push(10, 20, 30)
        res = self.st.pop()
        self.assertEqual(res, 30)
        self.assertEqual(self.st.peek(), 20)

    def test_pop_on_empty_stack(self):
        with self.assertRaises(IndexError):
            res = self.st.pop()
    
    def test_peek_on_empty_stack(self):
        self.assertTrue(self.st.is_empty())
        with self.assertRaises(IndexError):
            res = self.st.peek()