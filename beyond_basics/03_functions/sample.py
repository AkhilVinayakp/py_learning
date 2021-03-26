class Test:
    def __init__(self) -> None:
        print("init")
    @classmethod
    def __call__(cls):
        print('call')
    def __call__(self):
        print('instance call')

t = Test()
t()