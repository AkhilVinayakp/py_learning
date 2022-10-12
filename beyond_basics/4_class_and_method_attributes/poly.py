class Alpha:
    def greeting(self):
        print("greetings from Alpha class")

class Beta(Alpha):
    def greeting(self):
        print("greeting from the child class of Alpha - Beta")

a = Alpha()
a.greeting()
a = Beta()
a.greeting()