# Assign tasks to workers so that the time it takes to complete all 
# the tasks is minimized given a count of workers and an array where
# each element indicates the duration of a task.
# each worker must do 2 tasks

# using greedy approch ie. sort the array and pairing two end values

from typing import List
def opt_work(work_hour:List)->List:
	work_hour = sorted(work_hour)
	ret_list = []
	for i in range(len(work_hour)//2):
		ret_list.append((work_hour[i], work_hour[~i]))

	return ret_list


work_hour = [6, 3, 2, 7, 5, 5]
r = opt_work(work_hour)
print(r)
print(max(list(map(sum,r))))