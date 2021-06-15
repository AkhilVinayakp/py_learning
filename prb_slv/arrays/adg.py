#  Array advance game
# we have an array such that Each 
# number in the array represents the maximum you can advance in the array.
# Task is to find Is it possible to advance from the start of the array to 
# the last element given that the maximum you can advance from a position is
 # based on the value of the array at the index you are currently present on?
import logging
logging.basicConfig(level = logging.DEBUG, format =" %(levelname)s: %(asctime)s: %(message)s")

class Advance:
    '''
    '''
    def __init__(self,l):
        self.list = l

    def adv(self):
        #go through each element in the list and find the maximum can be
        # reached from it;
        max_reached = 0
        l_index = len(self.list)-1
        i = 0

        while i <= max_reached and i < l_index:
            max_reached = max(max_reached, self.list[i] + i)
            logging.debug(f"{max_reached} from index {i}")
            i = i+1
        return max_reached >= l_index


A = [3, 3, 1, 0, 0, 0, 1]
ad = Advance(A)
print(ad.adv())