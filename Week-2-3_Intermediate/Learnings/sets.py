# Note : sets are immutable, they are unordered and do not allow duplication
# https://youtu.be/l3kCO8cVA6o?si=aHTK1MY5JLYF58wf
# https://youtu.be/HOrutCnp2zo?si=ylMe0x1SD_grLciq

# sets = {1,2,3,4}
# print(sets)

sets2 = {}
print(type(sets2)) # output : dict

sets3 = set()
print(type(sets3)) # output : set

# A Loop and conditionals are works like in list


# --------- Set Methods: ----------
# 1. union and update:
# s1 = {1,2,3,4,5,6}
# s2 = {2,3,4,5,6,7}
# s1.update(s2)
# print(s1.union(s2))

# 2. intersection and intersection update:
# s1 = {1,2,3,4,5,6}
# s2 = {2,3,4,5,6,7}
# s1.intersection_update(s2)
# print(s1.intersection(s2))

# 3. Symmetic difference:
# s1 = {1,2,3,4,5,6}
# s2 = {2,3,4,5,6,7}
# s1.symmetric_difference_update(s2)
# print(s1.symmetric_difference(s2))

# 4. Difference:
# s1 = {1,2,3,4,5,6}
# s2 = {2,3,4,5,6,7}
# s1.difference(s2)
# print(s1.difference(s2))

# 5. disjoint
# s1 = {1,2,3,4}
# s2 = {4,5,6,7}
# s1.isdisjoint(s2)
# print(s1.isdisjoint(s2))

# 6. superset
# s1 = {1,2,3,4}
# s2 = {4,5,6,7}
# s1.issuperset(s2)
# print(s1.issuperset(s2))