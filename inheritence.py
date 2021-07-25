class Intesteller:
    iq = 90
    char_type = "versatile"
    char_strength = 75

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hey! iam {}".format(self.name))

    def survive(self):
        print("Hey iam Survived")

    def updateStrength(self, value):
        self.strength = self.strength + value


##=====Inheritence part start

class Inception(Intesteller):
    def Dream(self):
        print("im Dreaming")


cooper = Intesteller("Dr.Cooper")
TARS = Intesteller("TARS")
coob = Inception("DR Coob")

cooper.introduce()
