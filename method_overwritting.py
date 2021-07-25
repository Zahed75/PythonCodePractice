class Intesteller:
    iq = 90
    char_type = "versatile"
    char_strength=75

    def __init__(self, name):
        self.name = name
        print("Hey im belongs to intesteller")

    def introduce(self):
        print("Hey! iam {}".format(self.name))

    def survive(self):
        print("Hey iam Survived in amar mariam raag kora")

    def updateStrength(self, value):
        self.strength = self.strength + value


##=====Inheritence part start

class Inception(Intesteller):
    ## method overridding
    def __init__(self,name):
        self.name=name
        print("Hey im belongs to inception")
    def survive(self):
        print("Hey iam Survived in inception mariam raag kora")

    def Dream(self):
        print("im Dreaming")


cooper = Intesteller("Dr.Cooper")
TARS = Intesteller("TARS")
coob = Inception("DR Coob")

# cooper.introduce()
coob.survive()
cooper.survive()