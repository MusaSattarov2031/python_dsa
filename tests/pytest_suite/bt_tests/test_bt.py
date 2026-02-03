import pytest

@pytest.mark.parametrize("fixture, expected_len", [
    ("empty_bt", 0),
    ("full_random_bt", 10),
    ("full_bt", 5)
])
def test_len(request, fixture, expected_len):
    bt = request.getfixturevalue(fixture)
    assert len(bt) == expected_len

def test_str(full_bt):
    assert str(full_bt) == "1 2 3 4 5"

def test_add_node(empty_bt):
    empty_bt.add_node(10)
    assert len(empty_bt) == 1
    assert str(empty_bt) == "10"

    empty_bt.add_node(5)
    assert len(empty_bt) == 2
    assert str(empty_bt) == "5 10"
