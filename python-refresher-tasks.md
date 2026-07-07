# Advanced Python Programming Tasks

## 🧩 Task 1: Advanced Number Inspector

**Concepts:** Functions, loops, conditionals, math, input validation

Write a program that accepts an integer from the user and determines:

- Even or Odd
- Prime
- Perfect Number
- Armstrong Number
- Palindrome Number
- Sum of digits
- Product of digits
- Reverse of the number

**Requirements**

- Each check must be implemented as a separate function.
- Do not use external libraries.
- Handle negative numbers.

**Challenge:** Print all numbers between `1` and `N` that satisfy at
least **three** of the above properties.

---

## 🧩 Task 2: List Statistics & Transformation

**Concepts:** Lists, loops, algorithms

```python
numbers = [12, -3, 45, 0, 45, 12, -8, 90, 23, 90, 5]
```

Without using `set()`, `sorted()`, `max()`, `min()`, `count()`, or
`collections`:

1.  Remove duplicates while preserving order.
2.  Remove negative numbers.
3.  Implement Bubble Sort or Selection Sort.
4.  Find maximum, minimum, second largest, and second smallest.
5.  Count the frequency of each element.
6.  Rotate the list to the right by `K`.
7.  Separate even and odd numbers while maintaining order.

---

## 🧩 Task 3: Run-Length Compression

**Concepts:** Strings, loops

Implement:

```python
compress(text)
decompress(text)
```

Example:

    Input:
    aaabbccccdd

    Compressed:
    a3b2c4d2

    Decompressed:
    aaabbccccdd

**Requirements**

- Compress only if it shortens the string.
- Support multi-digit counts (e.g. `a12`).

---

## 🧩 Task 4: Student Record Management System

**Concepts:** Dictionaries, nested dictionaries, functions

Create a menu-driven program.

Features:

- Add student
- Update marks
- Delete student
- Display report card
- Find topper
- Find subject topper
- Calculate class average
- Search student
- Sort students by average

Support any number of subjects.

---

## 🧩 Task 5: Text Analytics Tool

**Concepts:** File handling, dictionaries, strings

Given a text file:

Find:

- Total words
- Total lines
- Total characters
- Unique words
- Word frequencies
- Top 5 words
- Longest word
- Average word length
- Words appearing only once

Ignore punctuation manually and convert all words to lowercase.

Do not use `collections`, `Counter`, or regular expressions.

---

## 🧩 Task 6: Persistent CLI To-Do Manager

**Concepts:** Lists, dictionaries, functions, files

Each task contains:

```python
{
    "title": "Finish Assignment",
    "priority": "High",
    "completed": False
}
```

Menu:

1. Add Task
2. View Tasks
3. Search Task
4. Mark Complete
5. Delete Task
6. Sort by Priority
7. Save
8. Load
9. Exit

Automatically load tasks when the program starts.

---

## 🧩 Task 7: Banking System

Create a banking application with:

- Create account
- Deposit
- Withdraw
- Transfer money
- Check balance
- Delete account
- Transaction history

Save all accounts to a file.

---

## 🧩 Task 8: Library Management System

Store books in nested dictionaries.

Features:

- Add book
- Remove book
- Borrow
- Return
- Search by title
- Show available books
- Show borrowed books

Track borrower name and borrowing date.

---

## 🧩 Task 9: Matrix Operations

Implement manually:

- Addition
- Subtraction
- Multiplication
- Transpose
- Row sums
- Column sums
- Largest element
- Symmetric matrix check

Do not use NumPy.

---

## 🧩 Task 10: Contact Book

Features:

- Add
- Update
- Delete
- Search by name
- Search by phone
- List contacts alphabetically (implement your own sorting)
- Save to file
- Load from file

Prevent duplicate phone numbers.
