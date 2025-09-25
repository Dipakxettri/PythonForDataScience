# https://youtu.be/AY_3MOo8tHw?si=hHWIKqbXbKfUScvf
# https://youtu.be/gOMW_n2-2Mw?si=tf6BQQ4cGeAJjepD

heros = ["spiderMan", "thor", "hulk", "ironman", "captain america"]
print(heros)
print(heros[0])# Indexcing 



# ---- Slicing: ----
# print(heros[-1])
# print(heros[:-1])
# print(heros[0:])
# print(heros[0:-1])
# print(heros[0:2])


# ---- list are mutable (they are changeable): ----
# heros[0] = "batman"
# print(heros)

# heros[1:2] = "strange"
# print(heros)
# Output : ['batman', 's', 't', 'r', 'a', 'n', 'g', 'e', 'hulk', 'ironman', 'captain america']

# soln :
# heros[1:2] = ["strange"]
# print(heros)

# print(heros[1:1]) # output : []
# heros[1:1] = ["venom"]
# print(heros)

# heros[1:2] = [] # removing thor
# print(heros)


# ---- Looping and conditions in lists: ----
# for hero in heros:
#     print(hero)

# if ("thor" in heros):
#     print("thor is present")   
# else:
#     print("thor is not present")


# ---------- list methods: ----------
# 1. append : adds an element at the end of the list
# heros.append("black panther")
# print(heros)

# 2. pop : removes the last element from the list and returns 
# heros.pop()
# print(heros)

# 3. insert : adds an element at the given index 
# heros.insert(1, "black panther")
# print(heros)

# 4. remove : removes the given el ement from the list
# heros.remove("thor")
# print(heros)

# 5. copy : returns a shallow copy of the list
# heros2 = heros.copy()
# print(heros2)
# heros2.append("black panther")
# print(heros2)
# print(heros)

# 6. extend : adds the elements of a list (or any iterable), to the end of the current list
# heros2 = ["black panther", "doctor strange"]
# heros.extend(heros2)
# print(heros)



