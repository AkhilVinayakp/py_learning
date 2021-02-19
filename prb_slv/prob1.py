'''
Remove Nth Node From End of linked list
'''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

class Node:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next

class LinkedList:
    '''
    main class that create the linked list 
    '''
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, element) ->None:
        '''
        function to insert a node at the begining
        params
        -------
        element : The value of the node 
        '''
        node = Node(element, self.head)
        self.head = node
    
    def showList(self):
        '''
        print the current linked list
        '''
        cur = self.head
        l_list = ''
        while(cur):
            l_list += '::---> '+str(cur.value)
            cur = cur.next
        print(l_list)

class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head == None:
            return None
        if head and n == 1:
            return 
        if head.next.next is None:
            if n == 1:
                head.next = None
                return head
            elif n == 2:
                return head.next
        cur = head
        temp = None
        count = 1
        while cur.next:
            logging.debug(f"{count} > {cur.value} > {count % n-1 == 0}")
            if count % n-1 == 0 :
                temp = cur
                logging.debug(f"temp set {cur.value}")
            cur = cur.next
            count +=1
        print(temp.value, cur.value)


l = LinkedList()
l.insert(2)
l.insert(3)
l.insert(10)
l.insert(33)
l.insert(3232)
l.showList()
t = Solution()
t.removeNthFromEnd(l.head,2)