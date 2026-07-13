# 🐍 Lecture 2: Strings, Input/Output, and Branching

This section documents my learning notes and key code implementations for Lecture 2 of the MIT Introduction to Computer Science and Programming Using Python course.

---

## 🧭 Lecture Overview & Structure

| Section | Topic | Status |
| :--- | :--- | :---: |
| **01** | Recap & Memory Bindings | ✅ Completed |
| **02** | The String Object Type (`str`) | ✅ Completed |
| **03** | String Operations (Length & Slicing) | ✅ Completed |
| **04** | Immutability of Strings | ✅ Completed |
| **05** | Input / Output (I/O) Fundamentals | ✅ Completed |
| **06** | Branching Programs (Conditional Logic) | ✅ Completed |

---

## 📚 Detailed Lesson Notes

### 📌 Section 1: Recap & Memory Bindings
*   **Object Types & Variable Assignments**: Every object in Python has a specific type that dictates what operations are allowed on it. Variables do not store values directly; they bind a name to an object in memory. Evaluating expressions always happens from the right-hand side of the equals sign first, creating a new object, and then binding the variable name to it.
*   **Variable Rebinding Mechanics**: Evaluating expressions like `radius = radius + 1` grabs the current value of the variable, adds one to compute a completely new value, creates a brand new object in memory, and rebinds the name to this new object (losing the original binding).
*   **Storing Types as Objects**: Python allows storing type references. An expression like `var = type(5 * 4)` evaluates the inner math to an integer object, fetches its type via `type()`, and binds that type object to the variable.

### 📌 Section 2: The String Object Type (`str`)
*   **Definition**: A sequence of case-sensitive characters enclosed in quotation marks (letters, numbers, special symbols, or control characters like newlines).
*   **String Concatenation (`+`)**: Combining strings using the `+` operator takes characters from both sequences to build a brand new object. It does not automatically insert spaces unless explicitly instructed.
*   **String Repetition (`*`)**: The `*` operator works between a string and an integer (in either order) to repeat the character sequence a specified number of times into a new object.
*   **Type Casting & Errors**: Python throws a `TypeError` if you try to multiply a sequence by a non-integer. Explicit casting functions like `int()` must be used to convert numeric string variables before repeating them.

### 📌 Section 3: String Operations (Length & Slicing)
*   **String Length**: The `len()` command evaluates to a single integer value representing the total character count within the string.
*   **String Indexing**: Individual characters are grabbed using square brackets. Python uses zero-indexing (counting starts at `0`). Negative indices allow backward counting from the right side, where `-1` represents the last character. Out-of-bounds indexing triggers an `IndexError`.
*   **Substring Slicing**: Extracted using the syntax `s[start:stop:step]`. The slice runs up to, but does not include, the `stop` index.
    *   *Default Step*: Omitting step defaults to `1` (moving left-to-right).
    *   *Shorthand Hacks*: Leaving start and stop boundaries empty clones the string (`s[:]`). Using a step of `-1` (`s[::-1]`) reverses the string sequence entirely.
    *   *Backward Slicing*: A negative step runs execution from right to left.
    *   *Empty String Edge Case*: If parameters conflict (e.g., trying to move rightwards to an index that sits behind the start index), Python returns a safe empty string `""` instead of crashing.

### 📌 Section 4: Immutability of Strings
*   **Definition**: Strings are immutable, meaning they cannot be modified in-place once created in memory.
*   **Altering Strings**: Attempting direct modification (e.g., `s[0] = "b"`) throws a `TypeError`. To modify text, you must construct a brand new string object using expressions like slicing/concatenation and rebind the variable name.

### 📌 Section 5: Input / Output (I/O) Fundamentals
*   **Console vs. Script Output**: Typing expressions directly in the shell shows a value for inspection, but this is not true program output. When executing a script file, implicit value outputs will not appear.
*   **The `print()` Command**: Explicitly displays output to the user. Every execution of a `print` statement outputs the evaluated expression and automatically appends a newline character.
*   **Multi-Object Printing**: Separating multiple data types with commas within a single `print()` statement prints them sequentially on the same line, automatically inserting a single space character between them.

### 📌 Section 6: Branching Programs (Conditional Logic)
*   **Definition**: Branching moves away from purely linear code execution, allowing a program to test conditions and execute different code paths based on boolean values.
*   **Comparison Operators**: Expressions that evaluate to a boolean (`True` or `False`) value. Examples include `>`, `>=`, `<`, `<=`, `==` (equality test), and `!=` (inequality test).
*   **The Indentation Rule**: Python does not use curly braces to define code blocks. It relies strictly on indentation (typically 4 spaces or one tab after a colon). All statements sharing the same indentation level run together as a single block unit.
*   **Binary Branching (`if-else`)**: Evaluates the condition after `if`. If true, it runs the immediate block and skips the `else` block. If false, it completely skips the `if` block and executes the `else` block.

---

## 🔗 Learning Resources & Context
*   [MIT 6.100L Course Video](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/resources/6100l-lecture-2-multi-version-4_1_mp4/): Lecture source video tracking strings, basic I/O tracking, and structural execution rules.
*   [Courses Dash Board Notion](https://app.notion.com/p/Courses-Dash-Board-369ae1ece481807891afc9440a3114a0?p=39bae1ece48180b4abc9df294a8a4024&pm=s): Primary personal tracker mapping university-level computer science fundamentals.
