# Python DSA & Test Automation Laboratory

A comprehensive repository of fundamental Data Structures and Algorithms implemented from scratch in Python, verified using both **pytest** and **unittest**.

## 🎯 Purpose
The goal of this project is twofold:
1. **Academic Preparation:** Mastering DSA concepts in preparation for second-year computer engineering coursework.
2. **Quality Assurance Mastery:** Practicing the transition between traditional `unittest` and modern `pytest` frameworks.

---

## 🏗️ Project Structure
The project is organized by architectural layers to ensure a clean separation of concerns.

```bash
.
├── src/                    # Business Layer (Implementations)
│   ├── linked_list.py
│   ├── stack.py
│   └── algorithms/
│       └── sorting.py
├── tests/                  # Core Layer (Automation)
│   ├── test_unittest/      # Traditional Class-based tests
│   │   └── test_stack.py
│   └── test_pytest/        # Modern Functional tests
│       └── test_stack.py
├── conftest.py             # Pytest configuration & fixtures
└── pytest.ini              # Metadata and marker registration
```
--- 
### Singly Linked List Implementation

A custom Python implementation of a Singly Linked List, designed for pedagogical purposes in Data Structures and Algorithms. This project focuses on manual pointer management and Pythonic operator overloading to mimic native container behavior.
#### Core Features
    * Pythonic Access: Implements __getitem__ and __setitem__ to allow standard bracket indexing (list[i]).

    * Dynamic Sizing: Tracks internal size for O(1) length retrieval via len().

    * Pointer Manipulation: Includes standard and advanced operations like insertion, deletion, and in-place reversal.

    * Cycle Detection: Implements Floyd’s Cycle-Finding Algorithm (Tortoise and Hare) to identify loops within the structure.

#### Method Overview
| Category	    | Methods                                   |
|:--------------|:------------------------------------------|
| Insertion	    | append, prepend, insert_at                | 
| Deletion	    | pop, remove, delete_at                    | 
| Search	    | search, index_of, is_empty                | 
| Magic Methods	| __len__, __getitem__, __setitem__, __str__| 
| Advanced	    | reverse, has_cycle                        | 
#### Data Structure Architecture

The implementation consists of two primary classes:

    * Node: The building block of the list, storing a value and a reference to the next node.

    * LinkedList: The controller class managing the head reference and orchestration of node relationships.