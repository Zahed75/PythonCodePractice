class Test:
    def sum(self,a,b,c):

        s= a+b+c
        return s

obj=Test()
print(obj.sum(10,20,30))

#method overloading

class Test:
    def sum(self,a=None,b=None,c=None):  #None is use for default argument
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
            return s


obj=Test()
print(obj.sum(10,20,30))