
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(message)s')

# defining a Node class to handle both data and left and right childs
class Node:
    def __init__(self, value) -> None:
        self._value = value
        self._left = None
        self._right = None


# defing the binary tree class
class Bi_tree:
    def __init__(self, root:int) -> None:
        self._root = Node(root)

    def add_left(self, data):
        if self._root._left == None:
            self._root._left = Node(data)
        else:
            temp:Node = self._root
            while(temp._left):
                temp = temp._left
            # now we have the left node that have no left insert there
            temp._left = Node(data)

    def add_right(self, data):
        if self._root._right == None:
            self._root._right = Node(data)
        else:
            temp:Node = self._root
            while(temp._right):
                temp = temp._right
            temp._right = Node(data)
        


logging.debug("Testing 1")


    