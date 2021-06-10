"""
Implement the RecentCounter class:

    RecentCounter() Initializes the counter with zero recent requests.
    int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].

"""
from collections import deque
class RecentCounter:
	def __init__(self):
		self._queue = deque()

	def ping(self,t:int)->int:
		# appending the data
		self._queue.append(t)

		# now poping the queue
		while self._queue[0]< t - 3000:
			self._queue.popleft()

		return len(self._queue)


r = RecentCounter()
r.ping(3300)
r.ping(6000)