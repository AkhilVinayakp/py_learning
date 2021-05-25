from linked_list_v2 import *

print('jai')

class Linked_Merger(LinkedList):
	def merge(self, llist):
		"merge two linked lists"
		p = self.head
		q = llist.head
		s = None

		# setting the pointers for first time
		if p.value <= q.value:
			s = p
			p = p.next
		else:
			s = q
			q = q.next

		# now s will serve as the head for the new linked list
		new_head = s
		# looping through to set other nodes
		# logging.debug(s.showList())

		while p and q:
			if p.value <= q.value:
				s.next = p
				s = p # updating the pointer of s
				p = p.next # updating the pointer of p
				# logging.debug(f"{s.showList()}")

			else:
				s.next = q
				s = q # updating the s pointer
				q = q.next # updating the q pointer

		# the loop will end if any of the p or q becomes none then
		# the remaining list will be attached to the new linked list
		if not p:
			s.next = q 

		if not q:
			s.next = p

		self.head = s
		# return self.head

if __name__ == '__main__':
	k = Linked_Merger()
	k.from_list([0,7, 8,10])
	k.showList()

	t = Linked_Merger()
	t.from_list([1,5, 9])
	t.showList()
	k.merge(t)
	k.showList()
	t.showList()