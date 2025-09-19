# Note : Tuples are immutable in python

tup = (1,2,3,4)
print(type(tup)) # output: tuple

tup2 = (1)
print(type(tup2))# output: int 

tup3 = (1,)
print(type(tup3))# output: tuple

# Tuple Methods:
# 1. if we wanna update tuple we first have to convert tuple into list make changes and again convert it back to tuple:
# Ex:
# tuplee = (1,2,3,4)
# temp = list(tuplee)
# temp.append(5)
# temp.append(6)
# temp.append(9)
# temp.pop(0)
# tuplee = tuple(temp)
# print(tuplee)

# 2. count() -> counts a given value
# tup = (1,2,3,4)
# print(tup.count(4))
 
# 3. index()
# tup = (1,2,3,4)
# print(tup.index(4))
# print(tup.index(2,0,2))
# Throw error if value is not cresent in an tuple

# 4. len()
tup = (1,2,3,4)
print(len(tup))  

