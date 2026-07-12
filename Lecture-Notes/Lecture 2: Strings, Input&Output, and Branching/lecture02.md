# Lecture 2: Memory Bindings, Strings, and Branching Programs

A technical reference guide for Python foundations, covering object type systems, memory model bindings, advanced string operations, and control flow mechanics.

---

## 1. Objects & Memory Bindings

### Variable Assignment & Evaluation Order
Python evaluates expressions on the right-hand side (RHS) of the assignment operator (`=`) first, instantiates the resulting object in memory, and then binds the variable name to that memory address.

```python
pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
