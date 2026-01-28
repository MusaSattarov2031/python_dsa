import pytest

def test_len(empty_queue, full_queue):
    assert len(full_queue) == 3
    assert len(empty_queue) == 0

def test_str(empty_queue, full_queue):
    assert str(empty_queue) == "Start->End"
    assert str(full_queue) == "Start->30->20->10->End"

def test_enqueue(empty_queue):
    empty_queue.enqueue(10)
    empty_queue.enqueue(20)
    empty_queue.enqueue(30)
    assert str(empty_queue) == "Start->30->20->10->End"
    assert len(empty_queue) == 3

def test_dequeue(full_queue, empty_queue):
    full_queue.deque()
    assert len(full_queue) == 2
    assert str(full_queue) == "Start->30->20->End"
    with pytest.raises(IndexError):
        empty_queue.deque()

def test_is_empty(full_queue, empty_queue):
    assert not full_queue.is_empty()
    assert empty_queue.is_empty()

def test_front(full_queue, empty_queue):
    assert full_queue.front() == 10

    with pytest.raises(IndexError):
        empty_queue.front()