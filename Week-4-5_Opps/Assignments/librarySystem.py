class Library:
    books = ["Dsa","Java","Ai","C","Python","MP"]
    borro = []
    def borrowBook(self):

        while(True):
            self.bookName = input("Enter a book name you want to borrow : ")
            if(self.bookName in self.books):
                self.borro.append(self.bookName)
                self.books.remove(self.bookName)
                print(f"Book {self.bookName} is borrowed")
                break

            else:
                print("Enter a valid book that exist")
    
    def returnBook(self):
        self.bookName2 = input("Enter a book name you want to return : ")

        if(self.bookName2 in self.borro):
            self.books.append(self.bookName2)
            print(f"Book {self.bookName2} is returned\n")

        else:
            print("The book was not borrowed last time\n")

    def main(self):
        while(True):
            print("\nSelect any one operation\n")
            self.operation = int(input("\nEnter 1 to borrow book\nENter 2 to return book\n:"))
            if(self.operation == 1):
                self.borrowBook()

            elif(self.operation == 2):
                self.returnBook()

            else:
                print("\nPlease enter a valid operation\n")
                
library = Library()
library.main()     

