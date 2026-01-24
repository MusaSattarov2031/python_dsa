import pytest

@pytest.mark.parametrize("fixture_name, expected_len", [
    ("empty_ll", 0),
    ("single_ll", 1),
    ("multiple_ll", 3)
])
def test_len(request, fixture_name, expected_len):
    ll = request.getfixturevalue(fixture_name)
    assert len(ll) == expected_len

def test_append(empty_ll):
    empty_ll.append(10, 20, 30)
    assert(len(empty_ll)==3)
    assert(empty_ll[0] == 10)
    assert(empty_ll[1] == 20)
    assert(empty_ll[2] == 30)

def test_prepend(ll_all_cases):
    init_size = len(ll_all_cases)
    ll_all_cases.prepend(10)
    assert(ll_all_cases[0] == 10)
    assert(len(ll_all_cases) == init_size+1)

def test_insert_at(empty_ll, single_ll, multiple_ll):
    empty_ll.insert_at(10, 0)
    assert(len(empty_ll) == 1 and empty_ll[0] == 10)

    single_ll.insert_at(20, 1)
    assert(len(single_ll) == 2 and single_ll[1] == 20)

    multiple_ll.insert_at(15, 1)
    assert(len(multiple_ll) == 4 and multiple_ll[1] == 15)

    with pytest.raises(IndexError):
        multiple_ll.insert_at(0, -1)
    
    with pytest.raises(IndexError):
        multiple_ll.insert_at(50, 7)
 
def test_pop(empty_ll, multiple_ll):
    with pytest.raises(IndexError):
        empty_ll.pop()
    res = multiple_ll.pop()
    assert(len(multiple_ll)==2 and res == 30)

def test_remove(multiple_ll):
    # case 1: remove from head
    multiple_ll.remove(10)
    assert multiple_ll[0] == 20
    assert len(multiple_ll) == 2

    # case 2: remove from middle
    multiple_ll.prepend(10)
    multiple_ll.remove(20)
    assert multiple_ll[1] == 30
    assert len(multiple_ll) == 2

    # case 3: remove from tail
    multiple_ll[1] = 20
    multiple_ll.append(30)
    multiple_ll.remove(30)
    with pytest.raises(IndexError):
        val = multiple_ll[2]
    assert len(multiple_ll) == 2

def test_delete_at(multiple_ll):
    with pytest.raises(IndexError):
        multiple_ll.delete_at(4)

    res = multiple_ll.delete_at(1)
    assert(res == 20 and multiple_ll[1] == 30 and len(multiple_ll) == 2)

def test_search(multiple_ll):
    assert(multiple_ll.search(10))
    assert(not (multiple_ll.search(40)))

def test_index_of(multiple_ll):
    assert(multiple_ll.index_of(10) == 0)
    assert(multiple_ll.index_of(40) == -1)

def test_is_empty(empty_ll, multiple_ll):
    assert(empty_ll.is_empty())
    assert(not multiple_ll.is_empty())

def test_reverse(multiple_ll):
    multiple_ll.reverse()
    assert(str(multiple_ll) == "30->20->10->None")

def test_has_cycle(multiple_ll):
    assert not multiple_ll.has_cycle()
    tail = multiple_ll.head
    while tail.next:
        tail = tail.next
    tail.next = multiple_ll.head
    assert multiple_ll.has_cycle()