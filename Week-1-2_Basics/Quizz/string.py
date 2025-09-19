# ------------ Quizz (Strings Related): ----------------
# -------- Q1. What is the output of: -------
# ```python
# s = "Python"
# print(s[::-1])
# ```
# a) Python
# b) nohtyP
# c) Error
# d) Pyt

# Ans = b


# ------- Q2. Write a Python program to count vowels in a given string: --------
s = "Python"
vowels = "aeiou"
count = 0
for char in s:
    if char in vowels:
        count += 1
        print(count)


# ---- Q3. Explain the difference between isalpha() and isdigit() methods: ----
# Ans : 
# isalpha checks if all characters in a string are alphabetic (letters only)
# isdigit checks if all characters in a string are digits (numbers only).   







