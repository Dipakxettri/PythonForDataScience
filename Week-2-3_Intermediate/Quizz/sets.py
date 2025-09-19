# Sets quiz


# ---------- Q1. Which of the following statements is false about sets? ---------
# a) Sets are unordered
# b) Sets allow duplicate values
# c) Sets are mutable
# d) Sets are defined using {}

# Ans: b


# -------- Q2. Write a Python program to find the union and intersection of two sets. --------
# Ans :
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8}
# union
unionSet = set1 | set2
print("Union:", unionSet)
# intersection
intersectionSet = set1 & set2
print("Intersection:", intersectionSet)

# ------- Q3. What is the output? --------
# ```python
# s = {1, 2, 3}
# s.add(2)
# print(s)
# ```

# Ans : {1, 2, 3} - because sets do not allow duplicate values