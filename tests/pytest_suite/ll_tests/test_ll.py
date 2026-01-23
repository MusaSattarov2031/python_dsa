import pytest

def test_len_of_empty_ll(empty_ll, single_ll, multiple_ll):
    assert(len(empty_ll) == 0)
    assert(len(single_ll) == 1)
    assert(len(multiple_ll) == 3)

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








