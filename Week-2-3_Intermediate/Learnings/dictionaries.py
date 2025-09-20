
# Key Value Pairs, ordered and muitable,

dict = {
    "first_name" : "deepak",
    "last_name" : "ghimire",
}
# print(dict["first_name"]) 


# dict["first_name"] = "Shyam"
# print(dict["first_name"]) 


# print(dict.get("last_name")) # results none 


# Difference ? :
# print(dict["last_name"]) # throw error if a key is't exist
# print(dict.get("last_name")) # results none 


# print(dict.keys())
# print(dict.values())

# for key in dict.keys():
#     print(dict[key])



#---- Dictionaries Methods: -----
eId1 = {1:2222,2:4444,3:3393,4:8888}
eId2 = {5:5628,6:6528}

# 1. Update():
eId1.update(eId2)
print(eId1)

# 2. Clear():
eId1.clear()

# 3. Pop():
eId1.pop(1)

# 4. popitem():
eId1.popitem()

# 5. del:
del eId1
del eId1[2]

