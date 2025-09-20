import random

def game():
    isRun = True
    while(isRun):
        player1 = input("Enter the name of player 1:")
        player2 = input("Enter the name of player 2:")
        isRun2 = True
        while(isRun2):
            r = random.randint(1, 9)
            try:
                guess1 = int(input(f"{player1} guess the number:"))
                guess2 = int(input(f"{player2} guess the number:"))

                if(guess1 == r and guess2 == r):
                    print("Draw\n")
                elif(guess1 == r):
                    print(f"{player1} Won\n")
                elif(guess2 == r):
                    print(f"{player2} Won\n")
                else:
                    print("\nNo one wins\n")
                
                operation = int(input("\nEnter 1 to play again\nEnter 2 to quit"))
                if(operation == 2):
                    isRun2 = False
                    isRun = False
                    
            except Exception as e:
                print("\nPlz enter a number\n")
            




game()
        
