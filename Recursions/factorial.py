# factorials using recursion
import time
import logging
from functools import wraps
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# execution time wrapper
def track(func):
    @wraps(func)
    def wrapper(*args):
        st_time = time.time()
        ret_value = func(*args)
        end_time = time.time()
        logger.info(f"Execution time: {end_time-st_time}")
        num_length = len(str(ret_value))
        if num_length > 20:
            return f'{num_length} digits'
        return ret_value
    return wrapper

class Factorial:
    def __init__(self, num:int) -> None:
        '''
        Args: 
            num(int) : number whoes factorial need to be calculated.
        Raises:
            (ValueError) : -ve numbers case.
        '''
        if num < 0:
            raise ValueError("can not instantiate object with a negative number.")

        self.number = num

    @track
    def fact_iteretive(self):
        '''
        Note:
            factorial using the iterative approach.

        '''
        if self.number <= 1:
            return 1
        else:
             fact = 1
             for i in range(2, self.number + 1):
                fact *= i
             return fact



# code execution
if __name__ == "__main__":
    f = Factorial(10)
    print('factorial by iterative approch:', f.fact_iteretive())