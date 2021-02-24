# implimentation of circular linked list 
# queue
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
class _Node:
    def __init__(self,value,next) -> None:
        self.value = value
        self.next = next

class NoItemException(Exception):
    pass

class CircularList:
    def __init__(self) -> None:
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    # Property to check empty or not
    @property
    def is_Empty(self):
        return self._size == 0
    @property
    def get_First(self):
        """ Return the first element from the queue
            Exception : No item exception
        """
        if self.is_Empty:
            raise NoItemException('no element found in the queue')
        head = self._tail.next
        return head.value
    def dequeue(self):
        """
        Remove the first Node and return it's value
        parameters:
        None
        Return:
        value of the first node
        Exception:
        NoItemException > in case the list is empty
        """
        if self.is_Empty:
            raise NoItemException("Queue empty")
        head = self._tail.next
        if self._size == 1:
            # list becomes empty while deleting the only elemet
            self._tail = None
            self._size = 0
        else:
            self._tail.next = head.next
            self._tail -= 1
        return head.value
    def enqueue(self):
        """
        Add a new element at the end
        parameter:
        value  
        Return : 
        None
        Exception:
        None
        """


    
    