# ==
# !=
# <
# >
# >=
# <=
# and
# or
# not
# is
# in
# True
# False

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, because a and b point to the same object in memory
print(a is c)  # False, because a and c are different objects, even though their values are the same


# in operator checks if a value is present in a sequence (like a list or a string)
if( 2 in a):
    print("2 is in a") 
else:
    print("2 is not in a") 