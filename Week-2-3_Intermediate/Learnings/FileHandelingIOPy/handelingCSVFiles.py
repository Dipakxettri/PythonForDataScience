# https://youtu.be/q5uM4VKywbA?si=9lWFrpVbAGSI-rP3
# Note: csv are coma seperated values

import csv
# with open("/home/sereynn/GitRepoes/PythonJourney-12Weeks/Week-2-3_Intermediate/Learnings/FileHandelingIOPy/students.csv","r") as file:

    # ---- Read: ----
    # csv_reader = csv.reader(file)

    #print(csv_reader)# returns a object we so we have to inerate throw it


    # ---- Write a conect of exesting csv file into another file with: ----

    # with open("/home/sereynn/GitRepoes/PythonJourney-12Weeks/Week-2-3_Intermediate/Learnings/FileHandelingIOPy/new_students.csv","w") as file2:
    #     csv_writer = csv.writer(file2, delimiter='-')
    #     # next(csv_reader)
    #     for line in csv_reader:
    #         csv_writer.writerow(line)


# ---- Practice: ----
# Q1. Read and Print CSV Contents
with open("/home/sereynn/GitRepoes/PythonJourney-12Weeks/Week-2-3_Intermediate/Learnings/FileHandelingIOPy/students.csv","r") as file:
    reading = csv.reader(file)
    for line in reading:
        print(line)

    




