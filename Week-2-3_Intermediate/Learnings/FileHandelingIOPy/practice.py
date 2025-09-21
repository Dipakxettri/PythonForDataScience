# -- Q no 1. Write a Python program to read first n lines of a file. --
# Ans :
# n = int(input("Enter the number of line you want to see:"))
# with open("/home/sereynn/GitRepoes/PythonJourney-12Weeks/Week-2-3_Intermediate/Learnings/FileHandelingIOPy/practice.txt","r") as file:
#     for i in range(n):
#         print(file.readline())

# -- Q no 2. Write a Python program to append text to a file and display the text. --
# with open("practice.txt","a+")  as file:
#     file.write("Hello new line added")
#     with open("practice.txt","r") as file2:
#         print(file2.read())

# -- Q no 3. Read Last N Lines. ----
# Ans : with deque =>
# from collections import deque
# with open("practice.txt","r") as file2:
#     print(deque(file2,2))

# With manual =>
# with open("practice.txt", "r") as file3:
#     for line in file3.readlines()[-0:]:
#         print(line)

# -- Q no 4. Write a Python program to read a file line by line and store it into a list. --
# list = []
# with open("practice.txt","r") as file4:
#     for line in file4.readlines():
#         list.append([line])

# print(list)

# -- Q no 5. Write a Python program to read a file line by line and store it into a variable. --
# with open("practice.txt","r") as file4:
#     for line in file4.readlines():
#         var = line
#         print(var)


# -- Q no 6. Write a python program to find the longest words. --
# with open("practice.txt") as file5:
#     words = file5.read().split()
#     longestWord = max(words, key=len)
# print(longestWord)

# -- Q no 7. Write a Python program to count the number of lines in a text file. --
# count = 0
# with open ("practice.txt","r") as file6:
#     for line in file6.readlines():
#         count += 1

# print(count)

# -- Q no 8. Write a Python program to write a list to a file. --
# lists = ["deepak","shyam"]
# with open ("practice.txt","w") as file7:
#     for list in lists:
#         file7.write(f"{list}\n")

# -- Q no 9. Write a Python program to copy the contents of a file to another file. --
# with open("practice.txt","r") as file1:
#     data = file1.read()
#     with open("test.txt","w") as file2:
#         file2.write(data)

# -- Q no 10. Write a Python program to read a random line from a file. --
# with open("practice.txt", "r") as file:
#     totalLines = 0

# -- Q no 11. Count Words in File. --
# Write a Python program that takes a text file as input and returns the number of words of a given text file.
# Note: Some words can be separated by a comma with no space.
# with open("practice.txt",'r') as file :
#     words = file.read().split()
#     print(len(words))

# -- Q no 12. Write a Python program to generate n text files named A.txt, B.txt, and so on up to Z.txt. --
# names = ["a.txt","b.txt","c.txt","d.txt"]
# for i in range(4):
#     with open(names[i],'w') as file:
#         file.write(f"file : {i}")
        