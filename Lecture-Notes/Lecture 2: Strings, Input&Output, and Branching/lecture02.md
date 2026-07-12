Markdown
# Lecture 2: Strings, Input/Output, and Branching

---

## Section 1: Recap & Memory Bindings

### 1. Object Types and Variable Assignments
Every object in Python has a specific type that dictates what operations are allowed on it. Variables do not store values directly; they bind a name to an object in memory. Evaluating expressions always happens from the right-hand side (RHS) of the assignment operator (`=`) first. A new object is created, and then the variable name is bound to it.

```python
pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
2. Variable Rebinding Mechanics
Rebinding evaluates the RHS using the current object values, computes a completely new value, creates a brand new object in memory, and rebinds the existing variable name to it. The binding to the original object is lost.

Python
radius = radius + 1
3. Storing Types as Objects
Python evaluates expressions inside functions first. The type() function evaluates to the object type itself. Because data types are also objects in Python, they can be stored inside variables just like any other value.

Python
var = type(5 * 4)
Section 2: The String Object Type (str)
A string is an immutable sequence of case-sensitive characters enclosed in quotation marks (" or '). Characters can include letters, numbers, special symbols, or control characters (like newlines or tabs).

Python
a = "me"
z = "you"
1. String Concatenation (+)
The + operator joins individual characters from both strings sequentially to create a brand new string object. It does not automatically insert spaces.

Python
b = "myself"
c = a + b
d = a + " " + b
2. String Repetition (*)
The * operator repeats a character sequence a specified number of times to create a new string object. It works between a string and an integer in either order.

Python
silly = a * 3
3. Type Casting & Type Errors
Python throws a TypeError if you attempt to multiply a sequence by a non-integer. To resolve this, you must explicitly cast a string containing numbers into an actual integer object using int().

Python
f = "a"
g = " b"
h = "3"

result = (f + g) * int(h)
# Error Scenario: (f + g) * h
Section 3: String Operations (Length & Slicing)
1. String Length (len())
The len() function evaluates to a single integer value representing the total number of characters (including spaces and symbols) contained within the string.

Python
s = "abc"
chars = len(s)
2. String Indexing
Indexing extracts individual characters using square brackets. Python uses zero-indexed positioning (counting starts at 0). Negative indices count backwards from the right, where -1 represents the last character. Indexing out of bounds throws an IndexError.

Python
# s = "abc"
print(s[0])
print(s[-1])
# Error Scenario: print(s[3])
3. Substring Slicing (Taking Chunks)
Slicing extracts a portion of a string using the syntax s[start:stop:step]. The execution extracts characters up to, but not including, the stop index. If omitted, the default step is 1.

Python
s = "abcdefgh"
Case A: Default Rightward Step

Omitting the step defaults to +1, moving left to right.

Python
print(s[3:6])    # Extracts indices 3, 4, 5
print(s[3:6:2])  # Skips every other character
Case B: Shorthand Hacks

Leaving boundaries empty copies the entire string. Using a step of -1 reverses the sequence.

Python
print(s[:])    # Full copy
print(s[::-1]) # Reverses the string
Case C: Backward Slicing Execution

A negative step moves execution from right to left.

Python
print(s[4:1:-2]) # Starts at index 4, steps backward by 2, stops before index 1
Case D: Empty String Edge Case

If boundaries conflict with the step direction, Python returns a safe empty string ("") instead of crashing.

Python
print(s[6:3]) # Tries to move right from index 6 to 3; returns ""
Section 4: Immutability of Strings
Strings are immutable, meaning they cannot be modified in-place once created in memory. Attempting an in-place modification throws a TypeError. To modify text, you must construct an entirely new string object using expressions like slicing and concatenation, then rebind the variable.

Python
s = "car"
# Error Scenario: s[0] = "b"

s = "b" + s[1:] # Correct approach via rebinding
Section 5: Input / Output (I/O) Fundamentals
⚠️ Note: Typing expressions directly in an interactive console displays values implicitly, but this is not true program output. In standard script execution, implicit expressions generate zero visible output.

Python
# Inside a file script, these execute silently:
len("abc")
"abc"[-1]
1. The print() Command Mechanics
To explicitly display output from a script file, expressions must be wrapped inside the print() command. Python automatically appends a newline character (\n) at the end of every executed print statement.

Python
print(len("abc"))
print("abc"[-1])
2. Multi-Object Printing
You can pass multiple objects of different data types into a single print() statement by separating them with commas. Python prints them sequentially on the same line, automatically separating them with a single space.

Python
print("the", 3, "musketeers")
Section 6: Branching Programs (Conditional Logic)
Branching allows a program to make decisions, test conditions, and execute different paths of code based on the truth value (True/False) of a boolean expression.

Python
x = 5
if x > 3:
    print("Greater")
else:
    print("Smaller or Equal")
1. Comparison Operators
Branching paths are triggered by expressions that evaluate to a boolean type (True or False):

i > j (Greater than)

i >= j (Greater than or equal to)

i < j (Less than)

i <= j (Less than or equal to)

i == j (Equality test — distinct from the single = assignment operator)

i != j (Inequality test)

2. The Indentation Rule & Code Blocks
Python relies strictly on indentation (4 spaces or 1 tab after a colon) instead of curly braces to define blocks of code. All statements sharing the same indentation level belong to the same block and execute together as a single unit.

3. Structure A: Simple Binary Branching (if-else)
If the condition evaluates to True, the if block executes and the else block is skipped. If it evaluates to False, the if block is skipped and the else block executes.

Python
if price < 100:
    print("Buy it immediately.")
else:
    print("Too expensive, do not buy.")
4. Structure B: Multi-Path Branching (if-elif-else)
Python evaluates conditions sequentially from top to bottom. The moment it encounters a condition that evaluates to True, it executes that specific block and skips the entire remaining chain of the conditional structure, even if subsequent conditions are also true.

Python
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B") # Execution stops here
elif score >= 70:
    print("Grade C")
else:
    print("Failing Grade")
5. Structure C: Nested Conditionals
Conditional blocks can be embedded inside other conditional blocks. Python monitors the depth of indentation levels to track which decision path a code block belongs to.

Python
x = 10
y = 20

if x == y:
    print("Equal")
else:
    if x > y:
        print("X is bigger")
        print("This is a nested statement")
    else:
        print("Y is bigger")
