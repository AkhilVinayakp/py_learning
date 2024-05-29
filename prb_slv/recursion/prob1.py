# %%
# we have 2 linked list in sorted order.
# we need to create a new linked list by combining these two and the final one should also in sorted order.

# example

# a = [1,3,6]
# b = [1, 2, 7]
# final = [1,1,2,3,6,7]
# %%
# implementation for a linked list
class Node:
    def __init__(self, value:int, _next=None):
        self.value = value
        self._next = _next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value:int)->None:
        """Append a new value"""
        node = Node(value=value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current._next:
                current = current._next
            # after the loop end we will find the last node.
            current._next = node
    def print_list(self):
        if not self.head:
            print("Empty list")
            return
        current = self.head
        while current:
            print(current.value, end='-->')
            current = current._next
        print("None")
# %%
l1  = LinkedList()
l1.append(1)
l1.append(4)
l1.append(6)
l1.print_list()

# %%
l2 = LinkedList()
l2.append(1)
l2.append(2)
l2.append(3)
l2.print_list()
# %%
# expected 
# 1-->1-->2-->3-->4-->6-->None
# %%
def merge_sorted(self, l1:LinkedList, l2:LinkedList):
    new_list = LinkedList()
    if l1.value >= l2.value:
        new_list, second_list = l1, l2
    else:
        new_list, second_list = l2, l1
    while new_list._next:
        new_list = new_list._next
        if new_list.value >= second_list.value:
            pass