# Q: Numbers divisible by 7 but not 5 between 1000–3000

# Input Number
for i in range(1000, 3001):
    if(i % 7 == 0 and i % 5 != 0):
        print(i)