import pytest
import random 
from src.binary_tree import BinaryTree

@pytest.fixture
def empty_bt():
    """Return an empty binary tree"""
    return BinaryTree()

@pytest.fixture
def full_random_bt():
    """Return a full binary tree with 10 random numbers between 0 and 100, and main root 50, included"""
    bt = BinaryTree()
    bt.add_node(50)
    for _ in range(10):
        n = random.randint(0, 100)
        if not bt.search(n):
            bt.add_node(random.randint(0, 100))
    return bt

@pytest.fixture
def full_bt():
    """Return a full bt, values: 1, 2, 3, 4 ,5"""
    bt = BinaryTree()
    bt.add_node(3)
    bt.add_node(1)
    bt.add_node(2)
    bt.add_node(5)
    bt.add_node(4)
    return bt

