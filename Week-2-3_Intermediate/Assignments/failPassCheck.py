# Q. Read student marks CSV → pass/fail :

import csv
with open("/home/sereynn/GitRepoes/PythonJourney-12Weeks/Week-2-3_Intermediate/Assignments/marks.csv") as file:
    data = csv.DictReader(file)
    for line in data:
        name = line["Name"]
        marks = int(line["Marks"])
        result = "Pass" if marks >= 40 else "Fail"
        print(f"{name} : {result} ")
    
        