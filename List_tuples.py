#List are mutable we can create edit list remove item etc
import copy

L_one=[1,2,3,4,5,6]
L_two=[6,47,9,2,3,5,9,10,13,12,15]
print(L_one)

"""
L_one.append("That thing i wanna say im sorry")
print(L_one)

L_two.sort()
print(L_two)
"""


L_two.pop()
print(L_two)

#copy function
L_three=copy.copy(L_one)
print(L_three)

L_three.remove(5)
print(L_three)


"""
Tuple are immutable user cannot the chage any obeject values
"""

name=('Zahed','mariam','Shihab','Afifa','Alisha')

print(name)

for x in name:
    print(x)

test_tuple=(1,2,3,4,5,6,7,8,9,10)
print(id(test_tuple))
test_tuple('python',2,3) #immutable
print(test_tuple)