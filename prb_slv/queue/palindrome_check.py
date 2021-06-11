#  code to check palidrom checker using deque

from collections import deque

def check_palindrome(stream: str)-> bool:
	stream = [ i for i in stream]
	dq = deque(stream)
	print(*dq)
	while True:
		try:
			if dq.popleft() != dq.pop():
				return False
		except IndexError as e:
			break
		except Exception as e:
			raise e
	return True	




s  = "radarii"
print(check_palindrome(s))
