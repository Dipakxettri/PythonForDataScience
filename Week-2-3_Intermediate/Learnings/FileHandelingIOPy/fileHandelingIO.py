import os
print("Current Working Directory:", os.getcwd())

# --------  What is File I/O? -----------
# File I/O stands for File Input/Output.
# Input (I) → Reading data from a file.
# Output (O) → Writing data to a file.


# ------- Open and Close a File: -------------
# Mode:
# 'r'	Read (default mode)
# 'w'	Write (overwrites if file exists)
# 'a'	Append (adds to the end of the file)
# 'x'	Create (fails if file exists)
# 'b'	Binary mode (use with other modes)
# 't'	Text mode (default)


# ---- Write: ----
# file = open("Week-2-3_Intermediate/Learnings/FileHandelingIOPy/test.txt", "r") # Open for writing
# file.write("Hello, world!")
# file.close() # Always close the file


# ---- read: ----
# file2 = open("test.txt", "r")
# print(file2.read())  # Reads everything
# file2.close()


# ---- some modes: -----
# 'r' -> open and read file (default)
# 'w' -> open file for writing, writes exestings data
# 'x' -> create a new file and open it for writing 
# 'a' -> open for writing, appending to the end of the file
# 'b' -> binary mode
# 't' -> text mode(default)
# '+' -> open a disk file for updating (reading writing )


# f = open("test.txt","r+")


# ----- read with parameter: -----
# data = f.read(2) 
# print(data)


# ---- read line: ----
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)


# ---- append: ----
# data = f.write("New data is added")


# ---- read and write: ----
# data = f.read()
# f.write("new line is added again")
# print(data)


# ---- with Statement: ----
# with open("test.txt", "r") as file:
#     content = file.read()# File is automatically closed outside the block


# ---- Deleting file: ----
# import os
# os.remove("test.txt")


# ---- Practice: ----
# 1. Printing text
# with open("practice.txt", "w") as practice:
#     practice.write("Hi everyone\nWe are learning File I/O\n")
#     practice.write("using Java.\nI love Java programming.")

# 2. Wap to replace all java words to python
# with open("practice.txt", "r") as practice2:
#     data = practice2.read()
# new_data = data.replace("Java", "Python")

# with open("practice.txt", "w") as practice2:
#     practice2.write(new_data)

# 3. Wap to find any word if it exists or not
# word = "python"
# with open("practice.txt","r") as practice3:
#     data = practice3.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not found")

# 4. wap to find a line number of any target element/word
target = "python"
line_no = 1
line = True
with open("practice.txt","r") as practice4:
    while line:
        line = practice4.readline()
    if(target in practice4):
       print(line_no)
    #    return 
    else:
        line_no += 1
    
print('hii')


