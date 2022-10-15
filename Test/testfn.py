
class Test:
    def __init__(self) -> None:
        self.__amount= 500
    @property
    def balance(self):
        return self.__amount
    @balance.setter
    def balance(self, amount:int):
        self.__amount = amount
    def __str__(self) -> str:
        return f"{self.__amount}"
    def __repr__(self) -> str:
        return f'current balance {self.__amount}'

t = Test()
print(t.balance)
t.balance = 200
print(t)
print(repr(t))
print(t._Test__amount)