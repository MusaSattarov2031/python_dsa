import unittest
from src.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.append(10, 20, 30)
        return super().setUp()
    
    def test_ll_append(self):
        #Testing ll.append by values 10, 20, 30
        ll = LinkedList()
        ll.append(10, 20, 30)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll[0], 10)
        self.assertEqual(ll[1], 20)
        self.assertEqual(ll[2], 30)


    def test_ll_str(self):
        ll = LinkedList()
        self.assertEqual(str(ll), "None")
        ll.append(10)
        self.assertEqual(str(ll), "10->None")

    def test_ll_pop(self):
        self.ll.append(10)
        res = self.ll.pop()
        self.assertEqual(len(self.ll), 3)
        self.assertEqual(res, 10)
        with self.assertRaises(IndexError):
            for _ in range(4):
                self.ll.pop()
    
    def test_prepend(self):
        self.ll.append(10, 20, 30)
        self.ll.prepend(5)
        self.assertEqual(self.ll[0], 5)
        self.assertEqual(len(self.ll), 7)
    
    def test_insert_at(self):
        self.ll.insert_at(5, 0)
        self.ll.insert_at(15, 2)
        self.ll.insert_at(50, 5)
        self.assertEqual(len(self.ll), 6)
        self.assertEqual(self.ll[0], 5)
        self.assertEqual(self.ll[2], 15)
        self.assertEqual(self.ll[5], 50)
        with self.assertRaises(IndexError):
            self.ll.insert_at(4, -1)
        with self.assertRaises(IndexError):
            self.ll.insert_at(50, 8)

    def test_remove(self):
        self.ll.remove(20)
        self.assertEqual(self.ll[0], 10)
        self.assertEqual(self.ll[1], 30)
        self.assertEqual(len(self.ll), 2)

    def test_delete_at(self):
        self.ll.delete_at(1)
        self.assertEqual(self.ll[0], 10)
        self.assertEqual(self.ll[1], 30)
        self.assertEqual(len(self.ll), 2)
        with self.assertRaises(IndexError):
            self.ll.delete_at(3)
        with self.assertRaises(IndexError):
            self.ll.delete_at(-1)
    
    def test_search(self):
        self.assertTrue(self.ll.search(10))
        self.assertFalse(self.ll.search(60))

    def testindex_of(self):
        self.assertEqual(self.ll.index_of(10), 0)
        self.assertEqual(self.ll.index_of(20), 1)
        self.assertEqual(self.ll.index_of(30), 2)
        self.assertEqual(self.ll.index_of(50), -1)
    
    def test_reverse(self):
        self.ll.reverse()
        self.assertEqual(str(self.ll), "30->20->10->None")

    def test_has_cycle(self):
        self.assertFalse(self.ll.has_cycle())
        curr = self.ll.head
        while curr.next != None:
            curr = curr.next
        curr.next = self.ll.head
        self.assertTrue(self.ll.has_cycle())


