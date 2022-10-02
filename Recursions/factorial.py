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
    def wrapper(number):
        if number < 0:
            '''not defined for negative values'''
            raise ValueError("not defined for negative values")
            return None
        st_time = time.time()
        ret_value = func(number)
        end_time = time.time()
        logger.info(f"Execution time: {end_time-st_time}")
        num_length = len(str(ret_value))
        if num_length > 20:
            return f'{num_length} digits'
        return ret_value
    return wrapper



@track
def fact_iteretive(number):
    '''
    Note:
        factorial using the iterative approach.

    '''
    fact = 1
    for i in range(2, number + 1):
        fact *= i
    return fact

@track
def recursive(number):
    '''Recursive approch 
    
    '''
    if number <= 1:
        return 1
    return recursive(number-1) * number


# code execution
if __name__ == "__main__":
    print('factorial by iterative approach:', fact_iteretive(12))
    print('factorial by recursive approach:', recursive(12))