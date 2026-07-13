# ==========================================
# Lecture 2: Strings, Input/Output, and Branching
# Practical Code Examples for GitHub
# ==========================================

# ------------------------------------------
# 📌 Section 1: Recap & Memory Bindings
# ------------------------------------------
pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
print("Initial Area:", area)

# Variable Rebinding Mechanics
radius = radius + 1
print("Rebound Radius:", radius)

# Storing Types as Objects
var_type = type(5 * 4)
print("Stored Type Object:", var_type)  # Output: <class 'int'>


# ------------------------------------------
# 📌 Section 2: The String Object Type (str)
# ------------------------------------------
a = "me"
z = "you"

# String Concatenation (+)
b = "myself"
c = a + b
d = a + " " + b
print("Concatenation without space:", c)
print("Concatenation with explicit space:", d)

# String Repetition (*)
silly = a * 3
print("String Repetition:", silly)

# Type Casting (Preventing TypeErrors)
h = "3"
# Explicitly casting string to int before multiplying
result = (a + " ") * int(h)
print("Casted String Repetition:", result)


# ------------------------------------------
# 📌 Section 3: String Operations (Length & Slicing)
# ------------------------------------------
s = "abcdefgh"

# String Length
print("Length of string:", len(s))

# String Indexing
print("First character s[0]:", s[0])
print("Last character s[-1]:", s[-1])

# Substring Slicing syntax -> s[start:stop:step]
print("Slice [3:6]:", s[3:6])        # Returns 'def' (excludes index 6)
print("Slice [3:6:2]:", s[3:6:2])    # Returns 'df' (skips by 2)

# Slicing Shorthands
print("Clone string s[:]:", s[:])      # Full copy
print("Reverse string s[::-1]:", s[::-1]) # Completely reverses characters

# Backward Slicing Execution
print("Backward slice [4:1:-2]:", s[4:1:-2]) # Returns 'ec'

# Structural Vacuum (Empty String Edge Case)
print("Invalid bounds slice [6:3]:", repr(s[6:3]))  # Returns empty string ''


# ------------------------------------------
# 📌 Section 4: Immutability of Strings
# ------------------------------------------
s_immutable = "car"
# Modifying a string requires creating a new object and rebinding
s_immutable = "b" + s_immutable[1:]
print("Modified through rebuilding:", s_immutable)  # Output: 'bar'


# ------------------------------------------
# 📌 Section 5: Input / Output (I/O) Fundamentals
# ------------------------------------------
# Multi-Object Printing automatically injects spaces between elements
print("The total count is:", 3, "items.")


# ------------------------------------------
# 📌 Section 6: Branching Programs (Conditional Logic)
# ------------------------------------------
x = 5

# Structure A: Simple Binary Branching (if-else)
if x > 3:
    print("Decision: Greater")
else:
    print("Decision: Smaller or Equal")

# Structure B: Multi-Path Branching (if-elif-else)
score = 85

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")  # Evaluated sequentially; halts structural checks here
elif score >= 70:
    print("Grade C")
else:
    print("Failing Grade")
