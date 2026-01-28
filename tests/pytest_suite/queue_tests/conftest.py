import pytest
from src.queue import Queue

@pytest.fixture
def empty_queue():
    """Test fixture for empty queue"""
    return Queue()

@pytest.fixture
def full_queue():
    """
    Test fixture for full queue, values Start->30->20->10->End
    """
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    return q