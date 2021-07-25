class Intersteller:
    iq = 90
    char_type = "varsatile"

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hey im {}".format(self.name))

    def survive(self):
        print("Hey im survive")

    def updateStrength(self, value):
        self.strength = self.strength + value


# INHERITENCE

class Inception(Intersteller):

    def Dream(self):
        print("amar ghumate eccha kore na")


Zahed=Intersteller("Full Stack Developer")
Mariam=Intersteller("Full Stack Developer")
Rafath=Inception("Mongo Expert")
Baby=Intersteller("Finally")


Zahed.introduce()
Mariam.introduce()
Rafath.Dream()
Baby.survive()
