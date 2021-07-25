# dictionary is like one of the data-structure of python
# its mutbale where user can put values as like list,tuples

student_inf = {
    "Name": 'Zahed Hasan',
    "BG": 'B+',
    "Contact": '012323124',
    "Color": "Black",
    "foods": ('Chicken', "pizaa", "coke")
}
# print(student_inf)

# print(student_inf['Name'])
#
# print(student_inf)

# access item
"""
x=student_inf["foods"]
print(x)

#get method
x1=student_inf.get("foods")
print(x1)

#key show
x1=student_inf.keys()
print(x1)
"""

# =====================

# semester = {
# "course": ['Python','Java','Ruby','WebDevelopment'],
# "department": "CSE",
# "year": "2021"
# }
#
# x = semester.items()
#
# print(x) #before the change
#
# semester["year"] = 2020
#
# print(x) #after the change
#


semester = {
    "course": ['Python', 'Java', 'Ruby', 'WebDevelopment'],
    "department": "CSE",
    "year": "2021",
}

if "course" in semester:
    print("Yes ,course in this semester")


#search item

inp_dict = {'Python': "A", 'Java': "B", 'Ruby': "C", 'Kotlin': "D"}

search_key = 'Ruby'

if search_key in inp_dict:
    print("The key is present.\n")

else:
    print("The key does not exist in the dictionary.")


#add item in dictionary

test={
    "subject":("ruby","pyhton","CSS"),
    "name":"Zahed Hasan",
    "id":43434
}

test["department"]="CSE"

print(test)