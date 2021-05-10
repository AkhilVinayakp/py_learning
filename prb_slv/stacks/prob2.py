# problem 2
# revesing a string using stack
# reverse a string using stack
from stack import *


def rev(string:str) -> str:
    '''function that takes a string as input and returns the reversed string as output'''
    s = Stack()
#      inserting each to the stack
    for i in string:
        s.push(i)
#     creates an empty string
    rev_str = ""
    while not s.isEmpty():
        rev_str += s.pop()
    return rev_str


if __name__ == "__main__":
    string = input('enter a string to reverse')
    print(rev(string))





