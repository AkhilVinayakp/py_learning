# the problem is part of Blind77
# https://leetcode.com/problems/merge-two-sorted-lists/description/

'''
<think>
Basically we have 2 sorted ll. we know the first value with the head address.
check which is the minimum 
head1.value < head2.value => new_head = head1

adjust the second element.
head.address.value < head2.value => no change. otherwise
head.address = head2 
'''
from dataclasses import dataclass
from typing import List

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

    @last_node.setter
    def last_node(self, trail: 'LinkedList'):
        self.last_node.next = trail.head

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
        current: Node = self.head
        while current:
            values.append(current.data)
            current = current.next
        print("List: \n  ", "--->".join([str(x) for x in values]) )

    def from_list(self, li: List):
        for item in li:
            self.insert(item)
        return self
    
    def merge_lists(self, other_list: 'LinkedList'):
        pass


def merge_lists(first: LinkedList, second: LinkedList) -> LinkedList:
    """
    Merge given 2 sorted linked lists and return the same
    we will be building additional one list.
    """
    sorted_ll = LinkedList()
    first_node = first.head
    second_node = second.head
    while first_node and second_node:
        if first_node.data <= second_node.data:
            temp_val = first_node.data
            first_node = first_node.next
        else:
            temp_val = second_node.data
            second_node = second_node.next
        sorted_ll.insert(temp_val)
    # checking whether any pending elements pending
    if first_node:
        sorted_ll.last_node = first_node
    if second_node:
        sorted_ll.last_node = second_node
    return sorted_ll


def main():
    first = LinkedList().from_list([1, 3, 5, 9])
    second = LinkedList().from_list([2, 4, 10])
    print("Input linked lists")
    first.print_nodes()
    second.print_nodes()
    merged_list = merge_lists(first=first, second=second)
    print("Merged list")
    merged_list.print_nodes()


if __name__ == "__main__":
    main()
