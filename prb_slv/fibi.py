import logging
from typing import List
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(message)s')


def fibi_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibi_rec(n-1)+fibi_rec(n-2)

def fibi_dp(n):
    memo:List = [None] * (n+1)
    memo[0], memo[1] = 0,1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo, memo[n]

logging.debug(fibi_rec(7))
# logging.debug(fibi_dp(7))