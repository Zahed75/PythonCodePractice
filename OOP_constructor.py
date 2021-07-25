'''
__init method__ constructor
'''
class Student: # creating class
    pass #> its defining empty

Zahed=Student() # its called Constructions > instantiation creating object/Constructor
Mariam=Student()
Alisha=Student()

'''
The constructor (__init__) -method /its automatically execute
The Constructor method speical method,attributes,inheritence
whenever you creating the objects of the class by default method will be call automatically

'''
# -=============== Execution objects============
class Student:
    def __init__(self,name,id,department):

        self.Name=name
        self.Id=id
        self.Department=department
        print("Hey im {},My id is {}, and my Department is {}".format(self.Name,self.Id,self.Department))
Zahed=Student("Zahed Hasan",75,"CSE") # its called Constructions > instantiation creating object/Constructor
Mariam=Student("Mariam Binte Mahfuz",53535,"CSE")
Alisha=Student("Alisha binte momin",553,"coming")


