# Triangle: 
# row = 5
# for i in range(1, row + 1):
#     for j in range(1, i + 1):
#         print("*", end="")

#     print()


# Diamond:
n = 5

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
