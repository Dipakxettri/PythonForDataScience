# def display():
#     print("Hello world")
# display()

# def sum(a,b):
#     print(a + b)
# sum(20,20)

# def sum(a,b = 20):
#     print(a,b)
# sum(40)

# def sum2(a = 20,b = 20):
#     print(a,b)

# sum2()
   

# ---------------------------- Recursion -------------------------
# - finding factorial: -
# factorial(10) = 10*9*8*7*6*5*4*3*2*1
# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(2))


# - Fibonaci Series: -
# Formula :
# F(0) = 0  
# F(1) = 1  
# F(n) = F(n-1) + F(n-2) 
# def fibonaciSeries(n):
#     if(n == 0):
#         return 0
#     elif(n == 1):
#         return 1
#     else:
#         return fibonaciSeries(n-1) + fibonaciSeries(n-2)
# print(fibonaciSeries(10))


# - Revise a Number -
def revise(num):
    if(num > 0):
        print(num)
        return revise(num -1)
revise(10)


# - Print Numbers from 1 to N: - 
def print1ToN(n):
    if(n == 0):
        return 
    print1ToN(n - 1)
    print(n)
print1ToN(10)

# --------------Resources:-------------------
# https://youtu.be/XYwJKFB8DUk?si=ZwRC-ua5tRPVb_qr
# https://developer.mozilla.org/en-US/docs/Glossary/Recursion
# https://en.wikipedia.org/wiki/Recursion_(computer_science)
# https://youtu.be/l8X9nhgZyoA?si=D1V-0g4XuNNnbZ2Q








