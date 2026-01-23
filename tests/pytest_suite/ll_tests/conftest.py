import pytest
from src.linked_list import LinkedList

@pytest.fixture(params=["empty", "single", "multiple"])
def ll_all_cases(request):
    ll = LinkedList()
    if request.param == "single":
        ll.append(10)
    elif request.param == "multiple":
        ll.append(10, 20, 30)
    return ll

@pytest.fixture
def empty_ll():
    return LinkedList()

@pytest.fixture
def single_ll():
    ll = LinkedList()
    ll.append(10)
    return ll

@pytest.fixture
def multiple_ll():
    ll = LinkedList()
    ll.append(10, 20, 30)
    return ll