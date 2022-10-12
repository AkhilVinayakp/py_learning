class Base:
    def __init__(self,name, age) -> None:
        self.__name = name
        self._age = age
    def SayHai(self):
        print(f"hai {self.__name}")

    @staticmethod
    def alert_fn():
        print("alert something went wrong")

class Child(Base):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)

    @staticmethod
    def say_thankyou():
        print("thank you")


b = Base('raj', 21)
b.alert_fn()
c = Child('raj', 21)
c.alert_fn()
