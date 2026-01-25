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

A custom Python implementation of a Singly Linked List, designed for pedagogical purposes in Data Structures and Algorithms.

### Stack
The Stack is a linear data structure that follows the LIFO principle. It is implemented using the LinkedList class to manage memory dynamically.