foods={
    "Street_food":('jhal Muri','Fuchka','vel puri','Pani puri'),
    "Spicy_food":('biriyani','kichuri','Mutton kabab'),
    "fruits":['mango','banana','strawberry'],

}
#
# foods.pop("Street_food")
# print(foods)

print("============")

x=foods.popitem()
print(x)

#========Delete item

del foods["Street_food"]
print(foods)

print("==========newline=============")

# del foods
# print(foods)


#==================Loop Dictionaries====================


foods={
    "Street_food":('jhal Muri','Fuchka','vel puri','Pani puri'),
    "Spicy_food":('biriyani','kichuri','Mutton kabab'),
    "fruits":['mango','banana','strawberry'],

}

# key print
# for x in foods:
#     print(x)

for y in foods:
    print(foods[y])

print("================4th line=======")

for m in foods.values():
    print(m)

#####################
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)