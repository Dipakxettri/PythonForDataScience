
# Key Value Pairs, ordered and muitable

dict = {
    "first_name" : "deepak",
    "last_name" : "ghimire"
}
# print(dict["first_name"]) 


# dict["first_name"] = "Shyam"
# print(dict["first_name"]) 


# print(dict.get("last_name")) # results none 


# Difference ? :
# print(dict["last_name"]) # throw error if a key is't exist
# print(dict.get("last_name")) # results none 


print(dict.keys())
print(dict.values())

for key in dict.keys():
    print(dict[key])



#---- Dictionaries Methods: -----



