
isRun = True

while(isRun):
    print("\nEnter the marks of all subjects")

    # Marks inputs
    c = int(input("Enter the marks of C Programming:"))
    dsa = int(input("Enter the marks of DSA:"))
    physics = int(input("Enter the marks of physics:"))
    ai = int(input("Enter the marks of AI:"))
    opps = int(input("Enter the marks of OPPS:"))
    dl = int(input("Enter the marks of Digital Logic:"))

    isRun2 = True
    while(isRun2):
        operation = int(input("\n\nEnter 1 to check Percentage\nEnter 2 to check GPA\nEnter 3 to enter Marks again\nEnter 4 to quit:"))

        # calculate GPA and percentage 
        totalObtainedMarks = c + dsa + physics + ai + opps + dl
        percentage = (totalObtainedMarks / 600) * 100
        gpa = (percentage / 100) * 4

        # Check Operations
        if(operation == 1):
            print("\nPercentage:",percentage, "%\n")
        elif(operation == 2):
            print("\nGPA:",gpa, "\n")
        elif(operation == 3):
            isRun2 = False
        elif(operation == 4):
            isRun2 = False
            isRun = False

            
            
            
