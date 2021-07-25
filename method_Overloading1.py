class Myclass:
    def sum(self, a, b, c):
        s = a + b + c
        return s


obj = Myclass()
print(obj.sum(10, 20, 30))
print(obj.sum(10, 20, 80))
print(obj.sum(10, 20))


# METHOD OVERLOADING

class MyClass:

    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        else:
            s = "Please vai atlst duita value de"
        return s




obj = MyClass()

print(obj.sum(10))
