"""
student_info = {
    "name": "Mariam Binte",
    "BG": "AB+",
    "ph": 434303434,
    "foods": ("chips", "pizza", "coke", "ice cream")

}

print(student_info)
# =========access
print(student_info["name"])
# ============access
x = student_info["foods"]
print(x)

# ========get method

x1 = student_info.get("ph")
print(x1)

# show keys=========
x2 = student_info.keys()
print(x2)

"""

#===============================

semester={
    "course":["C","C#","Python","Java","Data structure"],
    "department":"CSE",
    "year": 2021,

}

x=semester.items()
print(x)

#values change

# semester["year"]=2022
# print(semester)
#
# # SEARCH KEY
# if "ruby" in semester:
#     print("yes, course in this dictionary")
#
# else:
#     print("no elements in this dict")


######################################


# language = {"python","Javascript","ruby","Kotlin","Django","Swift"}
#
# search_key=("")
#
# if search_key in language:
#     print("yes item in this language")
