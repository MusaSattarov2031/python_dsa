import pytest

def test_len(empty_st, full_st):
    assert len(empty_st) == 0
    assert len(full_st) == 3

def test_str(empty_st, full_st):
    assert str(empty_st) == ""
    assert str(full_st) == "Top->30->20->10"

def test_push(empty_st):
    empty_st.push(20)
    assert empty_st.peek() == 20
    empty_st.push(30)
    assert empty_st.peek() == 30
    assert len(empty_st) == 2

def test_pop(empty_st, full_st):
    with pytest.raises(IndexError):
        empty_st.pop()
    res = full_st.pop()
    assert res == 30
    assert full_st.peek() == 20
    assert len(full_st) == 2

def test_is_empty(empty_st, full_st):
    assert empty_st.is_empty()
    assert not full_st.is_empty()
    for _ in range(len(full_st)):
        full_st.pop()
    assert full_st.is_empty()