import argparse 
import logging
from os import name
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# double linked list implimentations
class _Double_linked:
    class _Node:
        __slots__ = '_element', '_prev','_next'
        def __init__(self, element, prev, next) -> None:
            self._element = element
            self._prev = prev
            self._next = next
    # constructor for the _Double_linked list
    def __init__(self) -> None:
        # header node
        self._header = self._Node(None,None,None)
        # trailer node
        self._trailer = self._Node(None, None, None)
        # creaating the empty list header connected to the trailer
        self._header._next = self._trailer
        self._trailer._prev = self._header
        # initiating the size of the linked list as 0
        self._size = 0
    # overiding the __len__ function that will return the length of the linked list
    def __len__(self):
        return self._size
    # checking the list is empty
    @property
    def isEmpty(self):
        return self._size == 0
    # function to insert the a new node in between
    # insert with specifing the previous and next node
    def _insert_between(self,e, prev, next) -> _Node:
        temp = self._Node(e,prev,next)
        prev._next = temp
        next._prev = temp # setting up the linkes that makes the new node inbetween the prev and next
        # incrementing the size of the linked list
        self._size +=1
        return temp
    
    # deleting a specific node that return a value
    def _delete_node(self,node:_Node):
        prev = node._prev
        next = node._next
        prev._next = next
        next._prev = prev
        self._size -= 1
        return node._element
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    


        