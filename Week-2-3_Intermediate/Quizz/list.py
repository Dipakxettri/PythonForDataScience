# List Quiz


# ---------- Q1. What is the output of the following code? -----------
# ```python
# lst = [1, 2, 3]
# lst.append([4, 5])
# print(len(lst))
# ```
# a) 3
# b) 4
# c) 5
# d) Error

# Ans: b -> because append adds the entire list as a single element


# -------- Q2. Write a Python program to remove duplicates from a list. -----------
# Ans:
originalList = [1,2,2,3,4,5,6,7,8]
anotherList = []

for item in originalList:
    if(item not in anotherList):
        anotherList.append(item)

print(anotherList)


# -------- Q3. Explain the difference between append() and extend() with examples. --------
# append: adds the element at the end of list
# extend: adds the elements of lits at the end of list


