def PalindromeChecker(word):
    if(len(word) == 1):
        print("Palindrome")
    elif(word == word[::-1]):
        print("Palindrome")
    else:
        print("Not Palindrome")

PalindromeChecker("Deepak")
PalindromeChecker("bcdcb")

