word = 'i'
with open("/home/sereynn/GitRepoes/PythonJourney-12Weeks/Week-2-3_Intermediate/Assignments/file.txt",'r') as file:
    content = file.read().lower()
    count = content.count(word)
    print(count)


