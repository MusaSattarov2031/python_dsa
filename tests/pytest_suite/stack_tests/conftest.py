import pytest
from src.stack import Stack

@pytest.fixture
def empty_st():
    """
    Test Fixture for empty stack
    """
    return Stack()

@pytest.fixture
def full_st():
    """
    Test Fixture for full stack, values Top->30->20->1
    """
    st = Stack()
    st.push(10, 20, 30)
    return st