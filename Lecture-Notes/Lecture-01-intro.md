# 📝 Lecture 1: Introduction to Computation & Python

## 🛠️ Section 1: Course Strategy & Output

### 📑 Lectures & Practice
> 💬 **"Programming is actually a skill... It's something that you have to practice. You can't just watch me type... You need to do it often so that it becomes second nature."**
> 
> * **Key Takeaway:** Programming is an active, practical skill similar to playing a musical instrument or training for sports. True proficiency cannot be attained through passive consumption; it requires constant hands-on coding, encountering errors, and repetition until execution becomes subconscious.

### 🎯 The Three Pillars of Success
Mastering computational sciences relies heavily on three interconnected operational areas:

1. **Knowledge of Concepts:** Comprehending the abstract foundational principles and scientific models (primarily evaluated through lectures, quizzes, and examinations).
2. **Programming Skill:** Building the muscle memory required to fluidly map logic to syntax (developed sequentially through frequent, quick **Finger Exercises**).
3. **Problem Solving Skills:** The advanced capability to bridge human-readable specifications with functional code (deconstructing real-world prose, mapping it to core Computer Science methodologies, and engineering the programmatic solution via strict **Problem Sets**).

---

## 🧠 Section 2: Computational Thinking & Knowledge Types

### 💻 Computational Thinking
> 💬 **"How can I apply computation to help me solve this problem?"**
> 
> * **Key Takeaway:** Shifting perspective away from solving mathematical or logic problems manually using traditional workflows. Instead, the focus is on structuring algorithmic strategies that leverage the automated speed, memory, and parallel execution capabilities of modern hardware.

### 📚 Types of Knowledge
| Knowledge Type | Technical Definition | Computational Application |
| :--- | :--- | :--- |
| **Declarative Knowledge** | A statement of absolute fact. (e.g., *"The square root of a number $x$ is $y$ such that $y \times y = x$"*) | Outlines truth or the structural target, but inherently lacks an actionable blueprint or algorithmic instructions for execution. |
| **Imperative Knowledge** | A recipe; a detailed, chronological sequence of deterministic steps on how to execute a specific task. | Serves as the precise operational sequence that an interpreter or processing unit executes to evaluate an endpoint. |

### 📐 Algorithm
* **Definition:** A sequence of deterministic steps, driven by a structured flow of control, paired with an explicit, reachable stopping condition to guarantee termination.

---

## 🖥️ Section 3: How Computers Work (Low-Level Architecture)

### ⚙️ Computer Characteristics
> 💬 **"Computers are dumb. They don't make decisions on their own. They are just good at storing lots of data and doing operations really quickly."**
> 
> * **Key Takeaway:** Hardware possesses no intrinsic autonomy, generalized intelligence, or deductive reasoning. Computing power is fundamentally derived from two brute-force mechanical traits: massive low-latency data retention and rapid execution of raw mathematical primitives.

### 🏗️ Hardware Architecture Components
1. **Memory:** 
   * A sequential array of hardware registers where instructions and dynamic data primitives are allocated to explicit numerical addresses.
2. **ALU (Arithmetic Logic Unit):** 
   * The hardware engine responsible for computing mathematical evaluations (e.g., addition, subtraction, multiplication) and relational truth tests (comparisons).
3. **Control Unit:** 
   * Orchestrates the hardware execution loop. It updates the **Program Counter (PC)**, fetches the next prioritized instruction address from memory, and routes it to the native interpreter for execution.

---

## 🔤 Section 4: Language Elements (Python vs. Natural English)

### 1. Primitives
* **Natural English:** Individual baseline glyphs, characters, and standardized words.
* **Python:** Pre-defined native data types (numbers, string literals) and atomic logic operators (`+`, `-`, `*`, `/`, `==`, `>`).
* *Context:* The immutable, lowest-level architectural building blocks of the language syntax.

### 2. Syntax
* **Natural English:** Structural rules validating token placement. For example: `Noun + Verb + Noun` is structurally valid (*"Cat eats fish"*), whereas `Noun + Noun` is invalid (*"Cat dog"*).
* **Python:** Combines components to check code layout. The layout `object + operator + object` is valid (`"hi" * 5`), while running two unlinked primitives side by side is illegal (`"hi" 5`).

### 3. Static Semantics
* **Natural English:** Analyzes whether syntactically correct phrases convey proper context before parsing. For example: *"I are hungry"* passes layout check but violates structural agreement rules.
* **Python:** Identifies semantic conflicts prior to logical evaluation. Running `"hi" + 5` matches the basic structural layout (`object + operator + object`), but yields a compile-time/runtime **Static Semantic Error** (`TypeError`) because adding an integer directly to a string string breaks system typing rules.

### 4. Semantics
* **Natural English:** Inherently vulnerable to structural ambiguity, contextual overlap, and multi-layered interpretations (e.g., *"The chicken is ready to eat"*).
* **Python:** Completely deterministic. Code maps to exactly one executable path with zero systemic ambiguity. The computer implements the encoded instructions literally; if the code operates perfectly but outputs unexpected answers, a logical **Semantic Error** exists.

---

## 🐍 Section 5: Python Data Types & Expressions

### 📦 Objects & Types
> 💬 **"An object has a type. The type tells Python the things you are allowed to do with that object."**
> 
> * **Key Takeaway:** Every data initialization creates an encapsulated object. Its underlying data type acts as an explicit permission profile, defining valid structural interactions and functional limits.

### 📊 Scalar Objects (Primitives)
* **Integers (`int`):** Sign-aware whole numbers without fraction barriers (e.g., `5`, `0`, `-100`).
* **Float (`float`):** Mantissa-exponent real numbers carrying explicit decimal values (e.g., `3.27`, `2.0`).
* **Boolean (`bool`):** Strict binary truth assertions represented solely via `True` and `False` *(strictly case-sensitive)*.
* **NoneType (`NoneType`):** A single specialized type containing only one native literal value: `None` *(explicitly denoting the structural absence of value)*.

> 💡 **Utility:** The built-in `type()` function exposes the foundational type profile of any given object target (e.g., `type(7)` yields `<class 'int'>`).
> ⚠️ **Warning:** Deviating from explicit syntax conventions (e.g., entering lowercase `true`) breaks identifier mapping, instantly throwing a `NameError`.

### 🔄 Casting (Explicit Type Conversion)
> 💬 **"We are creating a new object in memory. We are not changing the original object."**
> 
> * **Key Takeaway:** Type casting functions construct a new object instance at a different memory location; they do not alter the source primitive.

* **Behavioral Matrix:**
  * `float(3)` $\rightarrow$ Evaluates to floating-point value `3.0`.
  * `int(5.9)` $\rightarrow$ Evaluates to `5`. This process performs a strict **truncation** of the decimal segment rather than a standard mathematical round.
  * `round(5.9)` $\rightarrow$ Evaluates to integer `6`. It processes standard rounding logic and cleanly modifies the resulting type profile to an implicit `int`.

### 📝 Expressions
> 💬 **"Python reads the expression, evaluates it to one single value, and then it stores the result value in memory. It never stores the expression."**
> 
> * **Key Takeaway:** Computational memory architecture is downstream of evaluation. Given a compound mathematical script (e.g., `3 + 2`), the runtime engine optimizes and reduces the complex token chain down to a localized scalar outcome (`5`) and caches the result value—discarding the structural math logic completely.

---
*Next Step: Proceeding to [Lecture 2: Strings, Input/Output, and Branching](./lecture-02-strings-branching.md) to manage programmatic control flow.*
