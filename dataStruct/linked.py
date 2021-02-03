class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next 



class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.head == None:
            return None
        else:
            i = 0
            tmp = self.head
            while(self.head):
                if i == index:
                    return tmp.val
                    break
                else:
                    tmp = tmp.next
                    i += 1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        t = Node(val = val)
        if self.head == None:
            self.head = t
        else:
            t.next = self.head
            self.head = t
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head == None:
            #adding at the beginig since the list is empty
            self.addAtHead(val=val)
        else:
            current = self.head
            while(current):
                if current.next == None:
                    t = Node(val)
                    current.next = t
                    break
                else:
                    continue

            
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)