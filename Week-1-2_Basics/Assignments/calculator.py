# Take inputs
num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2nd Number:"))
operator = input("Enter Operator:")
ans = 0

# conditionals to appaly operations
if(operator == "+"):
    ans = num1 + num2
elif(operator == "-"):
    ans = num1 - num2
elif(operator == "*"):
    ans = num1 * num2
else:
    ans = num1 / num2
