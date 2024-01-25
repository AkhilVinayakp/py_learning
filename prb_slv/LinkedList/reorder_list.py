#%%
# reorder a linked list
# link : https://leetcode.com/problems/reorder-list/description/
# date: 25-1-2024
# %%
# implementation of linked list
from dataclasses import dataclass
from typing import List
# %%
# defining the Node
@dataclass
class Node:
    data: any
    next: 'Node' = None


@dataclass
class LinkedList:
    head: Node = None

    @property
    def is_empty(self):
        return True if self.head is None else False
    
    @property
    def last_node(self):
        if self.is_empty:
            return None
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def insert(self, value)->None:
        """ Insert a Node at the end.
        Args:
            value(int) : input value
        """
        new_node = Node(data=value)
        if self.is_empty:
            self.head = new_node
        else:
            # adding at the end.
            last_node = self.last_node
            last_node.next = new_node
    def print_nodes(self):
        if self.is_empty:
            return "Empty linked list"
        values = []
        current:Node = self.head
        while current:
            values.append(current.data)
            current = current.next
        print("List: \n  ","--->".join([str(x) for x in values]) )
    
    def from_list(self, li:List):
        for item in li:
            self.insert(item)
        return self

# %%
llist = LinkedList()
llist.insert(23)
llist.insert(54)
llist.insert(65)
llist.print_nodes()
# %%
l1 = LinkedList().from_list([12,33,6,34])
l2 = LinkedList().from_list([9,18,90, 55])

print("current node structure")
l1.print_nodes()
l2.print_nodes()

# %%
# changing the structure.

