'''
You are also given an array queries where 
queries[j] = [xj, yj, rj] describes a circle centered 
at (xj, yj)
with a radius of rj.

For each query queries[j], compute the number of points 
inside the jth circle. Points on the border of the circle are 
considered inside.
1828
'''
from typing import List
import logging
import math

logging.basicConfig(level=logging.DEBUG, format= '%(levelname)s : %(message)s')

class Solution:
    def np_in_cirlce(self, points, queries):
        out = []
        for q in queries:
            count = 0
            logging.debug(f"sellecting the query {q}")
            for p in points:
                logging.debug(f"checking poin p {p} in {q}")
                d = math.sqrt((q[0]-p[0])**2 + (q[1]-p[1])**2)
                logging.debug(f"distance from origin{q[0],q[1]} is {d} and radius {q[2]}")
                if d<= q[2]:
                    count += 1
                    logging.debug(f"updating the count {count}")
            out.append(count)
        return out
                    
        



if __name__ == "__main__":
    s = Solution()
    points = [[1,3],[3,3],[5,3],[2,2]]
    queries = [[2,3,1],[4,3,1],[1,1,2]]
    print(s.np_in_cirlce(points, queries))