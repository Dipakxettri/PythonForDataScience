import os
import csv

#
def contactBook():
    isRun = True
    while(isRun):
        try:
              print(" \n---- Plz use select a operation from flowing ---- \n")
              operation = int(input("Enter operations\n Enter 1 for entering new contacts\n Enter 2 for checking contacts\n Enter 3 for quit\n :"))
        except Exception as e:
             print("\nplz enter a valid operation\n")

        if(operation == 1):
            try:
                name = input("Enter the name:")
                number = int(input("Enter the number:"))

                with open("contacts.csv","a") as contactBook:
                    data = csv.writer(contactBook)
                    data.writerow([name,number])
            except Exception as e:
                print("\nPlease enter a valid number again\n")

        elif(operation == 2):
            with open("contacts.csv","r") as contactBook2:
                    datas = csv.reader(contactBook2)
                    print("\nContacts:")
                    for dat in datas:
                         print(dat,"\n")

        elif(operation == 3):
             break
             isRun = False

        else:
             print("\nPlz enter valid operation\n")
            
            
contactBook()     
        