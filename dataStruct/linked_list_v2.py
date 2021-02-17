'''
Linked list implimentation
'''

class emptyException(Exception):
    pass

from typing import List


class Node:
    def __init__(self,value = None, next = None) -> None:
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

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
    def insert_end(self,element)-> None:
        '''
        Method to add an element at the end of the linked list
        '''
        if self.head == None:
            self.insert(element)
            return None
        cur = self.head
        while cur.next : # checking whether next node exit or not, if not cur is the last node
            cur = cur.next
        cur.next = Node(element)

    def pre_check(func):
        '''
        pre checking methods for other functions
        '''
        def inner(self,index,element):
            if self.head is None:
                raise emptyException
                return
            if len(self) < index:
                print('index out of range .')
                return
            return self.func(index,element)
        return inner

    @pre_check
    def ins_at(self,index,element):
        cur = self.head
        count = 0
        while cur:
            if count == index-1:
                cur.next = Node(element, cur.next)
                break
            cur = cur.next
            count += 1
    @pre_check
    def __setitem__(self,index,element):
        '''overriding for [] '''
        cur = self.head
        count = 0
        while cur:
            if count == index-1:
                cur.next = Node(element, cur.next)
                break
            cur = cur.next
            count += 1

    @pre_check
    def replace(self,index,element):
        cur = self.head
        cout = 0
        while cur:
            if cout == index: # checking whether there index reached
                cur.value = element
                break
            cur = cur.next
            cout += 1
    @pre_check
    def remove_at(self,index)->None:
        if index == 0:
            self.head = self.head.next
            return None
        cur = self.head
        count = 0
        while cur:
            if count == index-1:
                cur.next = cur.next.next
                return None
            cur = cur.next
            count += 1
        
    def index(self,data)-> int:
        ''' Returns the index of the puricular element'''
        cur = self.head
        count = 0
        index = None
        while cur:
            if cur.value == data:
                index = count
                break
            cur = cur.next
            count += 1

        return index
    
    def remove_data(self,data)->None:
        ''' Remove a purticular data '''
        index = self.index(data)
        if index is None:
            print('Data not found')
            return None
        self.remove_at(index)
    
    # overloading the getitem to return data at index
    def __getitem__(self, key):
        if self.head is None:
            print('list is empty')
        if key > len(self):
            print(f'{key} does not exist')
        cur = self.head
        count = 0
        value = None
        while cur:
            if count == key:
                value  = cur.value
                break
            cur = cur.next
            count += 1
        return value
    def from_list(self, values:List)-> None:
        if self.head is not None:
            print("Linked list should be empty try append_list")
            return
        values = values[::-1]
        for i in values:
            self.insert(i)
    # ToDO complete
    def reverse(self):
        if self.head is None:
            print('List is empty')
            return
        cur = self.head
        l = []
        while cur:
            l.append(cur.value)
    
        self.from_list(l)
        


if __name__ == '__main__':
    l = LinkedList()
    l.insert(3)
    l.insert(4)
    l.insert(42)
    l.showList()
    l.insert_end(20)
    
    l.showList()
    print(len(l))
    # l.ins_at(9,45)
    l[30] = 100
    l.showList()
    # print(len(l))
    print(l[2])
    print("From List")
    k = LinkedList()
    k.from_list([0,9,8,7])
    k.showList()
    print('reversed')
    k.reverse()
    k.showList()