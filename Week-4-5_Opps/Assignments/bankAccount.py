class Bank:

    amount = 2000
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def deposit(self,am):
        self.amount += am

    def withdraw(self):
        while (True):
            try:
                self.am2 = int(input("Enter a amount of money you want to withdraw:"))
                if(self.am2 != 0 and self.am2 <= self.amount):
                    self.amount -= self.am2
                    break

                else:
                    print("plz enter a sufficent amount")

            except Exception as e:
                print("Enter a valid amount")


    def getAmount(self):
        print(self.amount)

    def main(self):
        while (True):
            operation = int(input("Enter 1 for deposit:\nEnter 2 for withdraw:\nEnter 3 to check amount:\nEnter 4 for exit\n:"))
            
            if(operation == 1):
                self.deposit_money = int(input("Enter a anount of money you want to deposit:"))
                self.deposit(self.deposit_money)
            elif(operation == 2):
                self.withdraw()
            elif(operation == 3):
                self.getAmount()
            elif(operation == 4):
                break
            else:
                print("Enter valid operation")

user = Bank("deepak",12)
user.main()
      
    