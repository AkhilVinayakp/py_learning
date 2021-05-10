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

# exception raied when a stack contains non numeric values. used in Max property
class NotaNumberException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class Stack:
    '''
    contains the implimentation of stack and it's basic functionalities 
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
    # implimenting max property that will return the max element in the stack
    @property
    def Max(self)->int:
        max = -222222222222222222222222222222222
        for i in self.stk:
            if i > max:
                max = i
        return max

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

# testing script for Stack

s = Stack(limit=13)
s.push(1)
s.push(2)
s.push(43)
s.push(4)
s.push(5)
s.show()
print(s.Max)
s.show(reverse=True)
    

# implimenting Dynamic stack
# overcome overflow by using the approch repeated doubling : when the array is full we create a new array with
# the size double of the original array and copy all the elemets to the new array

class DynamicStack(Stack):
    '''  '''
    def __init__(self, limit: int) -> None:
        super().__init__(limit=limit)
    def push(self, item: int) -> None:
        if self.length >= self.limit:
            self.resize()
        return super().push(item)
    def resize(self):
        # crating a new space for the new list
        self.stk = list(self.stk)
        # doubling the limit 
        self.limit = 2 * self.limit

        
# tesing for dyanmic stack
s = DynamicStack(limit=3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.show()
s.show(reverse=True)

#TODO implimentation using linked list