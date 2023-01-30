# Sets and Frozen sets

# lists and sets are very similar
# sets are unordered

# create a set

car_parts = {"wheels", "door", "exhaust"}
print(car_parts)

# removing parts of a set

car_parts.discard("doors")
print(car_parts)
# add things to set
car_parts.add("windows")
print(car_parts)

# Frozen sets

# frozen sets are immutable (cant be changed) versions of a set. still inordered and un-indexed

x = frozenset([1,2,3,4, "five"])
print(x)


