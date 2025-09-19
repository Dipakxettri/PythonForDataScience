# ---- Data Types: ----
intiger = 20
string = "Deepak"
char = 'A'
float = 7.2
boolean = True # or False 

# String :
text = "Python"
print(text[0])  # P
print(text[-1]) # n (last character)


# ---- Variables: ----
# variables are the containers which stores values like 'a = 20' here a is variable which stores value 20.


# ----operators----:
# Arithmetic Operators:
add = 20 + 20
sub = 20 - 20
mult = 20 - 20
floatDivi = 20 / 20 # This results in float value 
floorDivi = 20 // 20 # This results in floor value
modulas = 9 % 2 # Results a reminder
exponentiation = 20 ** 20 

# Comparison (Relational) Operators:
isEqual = 20 == 20 # double == comapres two values where single = used for assignments
notEqual = 20 != 20 # opposite of double equal
greaterThen = 20 > 10
lessThen = 10 < 20
greaterThenEqualTo = 2 >= 2
lessThenEqualTo = 2 <= 2

# Assignment Operators:
# 1. '=' 
a = 20
# 2. '+=' => This operator first do  operation and assign the value. works for all operators
a += 80

# Logical Operators
# logical operator includes 'and, or, not' they are same as '&&, ||, !' in C and java.

# Ternary Operator:
num = 65
result = "Even" if x % 2 == 0 else "Odd"  #Output: "Odd"

a = 5
b = 6
result = "Both positive" if a > 0 and b > 0 else "At least one is non positive"
print(result)  # Output: Both positive


# ---- Conditionas: ----
# conditions helps program to make decisions
# if elif else
num1 = 90
num2 = 28
if(num1 > num2):
    print(f"the num1 : {num1} is greater then num2 : {num2}")
elif(num1 < num2):
    print(f"the num2 : {num2} is greater then num1 : {num1}")
else:
    print(f"Both num1: {num1} and num2: {num2} are equal")

# Note: just like in Java, C where we use '{}' to represent a block of code we use ':' in python.


# ---- Loops: ----
# loop are block of code that repets a specific task until the condition is True

# for loop
# Loop Throw numbers
for i in range(20):
    print(i) # prints from 0 to 19, python does't include a given value it is like saying (0 to 19) where python automatically place 0 as a start if we does't specify the start.
# specify the start 
for i in range(1,21):
    print(i)
# Loop Throw each characters of a string
name = "deepak"
for char in name:
    print(char)
# print any string multiple times
name2 = "deepak"
for i in range(20): 
    print(name)

# While Loop:
while(True):
    print("deepak")# infinite loop because condition is always true

isRun = True
i = 1
while(isRun):
    if(i >= 21):
        isRun = False
    else:
        print(i)
        i+=1

j = 1
while(True):
    if(i == 21):
        continue
    elif(j<=80):
        break

k = 0
while(True):
    k += 1
    if(k == 21):
        continue
    elif(k>=80):
        break
    print(k)






