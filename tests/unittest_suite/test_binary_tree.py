import unittest
import random
from src.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()
        return super().setUp()
    
    def test_len_and_add_node(self):
        self.assertEqual(len(self.bt), 0)

        self.bt.add_node(5)
        self.assertEqual(len(self.bt), 1)
        self.bt.add_node(10)
        self.assertEqual(len(self.bt), 2)
        self.bt.add_node(0)
        self.assertEqual(len(self.bt), 3)

    def test_str(self):
        self.assertEqual(str(self.bt), "")

        self.bt.add_node(5)
        self.bt.add_node(10)
        self.bt.add_node(0)

        self.assertEqual(str(self.bt), "0 5 10")

    def test_delete_at_edge(self):
        self.bt.add_node(5)
        for i in range(10):
            self.bt.add_node(i)
        
        #Test deleting at edges: 4 or 6
        self.bt.delete_node(4)
        self.assertEqual(str(self.bt), "0 1 2 3 5 6 7 8 9")
    
    def test_delete_in_middle(self):
        self.bt.add_node(5)
        for i in range(10):
            self.bt.add_node(i)
        
        self.bt.delete_node(0)
        self.assertEqual(str(self.bt), "1 2 3 4 5 6 7 8 9")

    def test_delete_head(self):
        self.bt.add_node(5)
        for i in range(10):
            self.bt.add_node(i)
        self.bt.delete_node(5)
        self.assertEqual(str(self.bt), "0 1 2 3 4 6 7 8 9")

    def test_search(self):
        self.bt.add_node(5)
        for i in range(100):
            self.bt.add_node(i)

        self.assertTrue(self.bt.search(random.randint(0, 99)))
        self.assertFalse(self.bt.search((random.randint(0, 99))*(-1)))
    
    def test_get_height(self):
        self.assertEqual(self.bt.get_height(), -1)
        self.bt.add_node(5)
        self.assertEqual(self.bt.get_height(), 0)

        for i in range(10):
            self.bt.add_node(i)

        self.assertEqual(self.bt.get_height(), 5)

    def test_as_list(self):
        self.bt.add_node(5)
        for i in range(10):
            self.bt.add_node(i)

        self.assertEqual(str(self.bt.as_list()), "[5, 0, 6, 1, 7, 2, 8, 3, 9, 4]")

    def test_clear(self):
        self.bt.add_node(50)
        for i in range(100):
            self.bt.add_node(i)
        self.bt.clear()
        self.assertEqual(len(self.bt), 0)


    def test_min_max(self):
        self.bt.add_node(50)
        for i in range(100):
            self.bt.add_node(i)
        self.assertEqual(self.bt.find_max(), 99)
        self.assertEqual(self.bt.find_min(), 0)
        self.bt.clear()
        with self.assertRaises(ValueError):
            MAX = self.bt.find_max()