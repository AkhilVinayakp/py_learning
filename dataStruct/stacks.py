# implimenatation of stack  using simple array 

# exception class
class OverflowException(Exception):
    """
    Exception raised when user try to insert element in stack if it is at it's limit
    Attributes:
    Message : error message
    """
    def __init__(self, message = 'Overflow :can not insert further elements') -> None:
        self.message = message
        super().__init__(self.message)
class UnderflowException(Exception):
    '''
    Exception raised when user try to remove element from an empty stack
    '''
    def __init__(self, message) -> None:
        super().__init__(message)

class Stack:
    '''
    contains the impimentation of stack and it's basic functionalities 
    v : 1.0
    '''
    def __init__(self, limit:int = 10) -> None:
        ''' create a Stack object with default size limit 10 '''
        self.stk = []
        self.limit = limit
    def isEmpty(self)-> None:
        '''function that checks the stack is empty or not'''
        return len(self.stk) <= 0
    @property
    def length(self)->int:
        return len(self.stk)
    def push(self, item:int)-> None:
        ''' method that push values to a stack'''
        if self.length >= self.limit:
            raise OverflowException
        self.stk.append(item)
        print(f'item inserted successfully {self.stk}')
    def pop(self)-> int:
        ''' delete the last inserted item from the stack and return '''
        if self.length <= 0:
            raise UnderflowException
        return self.stk.pop()
    def show(self, reverse = False)->None:
        ''' shows a stack '''
        if self.length <= 0:
            raise UnderflowException("no elements in the stack to show")
        if not reverse:
            items = iter(reversed(self.stk))
        else:
            items = iter(self.stk)
        print(f'[{next(items)}]  <--- Top')
        for i in items:
            print(f'[{i}]')

# testing
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.show()
s.show(reverse=True)
    

        

