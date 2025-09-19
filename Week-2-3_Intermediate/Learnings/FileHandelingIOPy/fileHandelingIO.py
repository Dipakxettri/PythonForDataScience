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
# file2 = open("Week-2-3_Intermediate/Learnings/FileHandelingIOPy/test.txt", "r")
# print(file2.read())  # Reads everything
# file2.close()


# ---- with Statement: ----
with open("Week-2-3_Intermediate/Learnings/FileHandelingIOPy/test.txt", "r") as file:
    content = file.read()# File is automatically closed outside the block
