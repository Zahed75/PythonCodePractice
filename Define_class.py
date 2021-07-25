class Student:
    pass

Zahed=Student()
Mariam=Student()
Suhaiba=Student()


'''
The Constructor (__init__)> magical method its automatically execute
special method 
'''

class Student:
    def __init__(self,name,id,bg): #self refers to current objects
        self.Name=name
        self.ID=id
        self.BG=bg # current objects
        print("Hey im {}, My id is {}, and My Blood Group is {}".format(self.Name,self.ID,self.BG))



Zahed=Student("Zahed Hasan",75,"B+")
Mariam=Student("Mariam Binte Mahfuz",8953,"AB+")
Suhaiba=Student("Mini Baby","coming soon","B+")
Alisha=Student("Alisha Binte Momin","coming soon","B+")