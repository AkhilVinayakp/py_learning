# array based 
'''
given an array  reorder its entries so that the even entries appear first
'''
import logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
class Solv:
    @staticmethod
    def twopointer(x):
        ''' solving using two pointer '''
        even , odd = 0 , len(x) - 1
        while(even < odd):
            if x[even] % 2 == 0:
                even += 1
            else:
                x[even],x[odd] = x[odd], x[even]
                odd -= 1
        return x

logging.debug("start")
s = Solv()
t = [3,2,4,6,2,1,7,85,43,24,4]
logging.debug(f"before{t}")
print(s.twopointer(t))

