# Python Recursion Examples

This repository contains Python examples that demonstrate how recursion works in different scenarios — from simple problems like factorial calculation to more advanced concepts like backtracking and divide-and-conquer algorithms.

## 📂 Project Structure


## ✅ Examples Included

- **factorial.py** — Calculate factorial of a number using recursion.
- **fibonacci.py** — Generate Fibonacci numbers recursively.
- **gcd.py** — Find the Greatest Common Divisor (GCD) using Euclidean algorithm.
- **sum_of_list.py** — Sum elements of a list recursively.
- **binary_search.py** — Perform a binary search using recursion.
- **tower_of_hanoi.py** — Solve Tower of Hanoi puzzle recursively.

## 🔍 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/python-recursion-examples.git
   cd python-recursion-examples
   ```
## 💡 What is Recursion?
Recursion is a programming technique where a function calls itself to solve smaller instances of a problem until it reaches a base case.

Example: Factorial


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        
## 🚀 Why Use Recursion?
Simplifies code for problems that can be broken down into smaller subproblems.

Useful for tree and graph traversal.

Foundation for many algorithms: DFS, backtracking, dynamic programming, etc.

## ⚠️ Note
Be careful: recursion can lead to stack overflow if the base case is not defined properly or if the recursion depth is too large.

# 📚 References
Python Official Documentation - Recursion

Wikipedia - Recursion
