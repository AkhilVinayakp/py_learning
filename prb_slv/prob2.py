'''
what is the maximum number of characters, between any two same characters in the string.
'''
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('start')
# logging.disable(logging.CRITICAL)
n = int(input())
sl = [input() for _ in range(n)]
logging.debug(f'{sl}')
l = []
for s in sl:
    li = []
    l_max = 0
    for j in range(len(s)-1):
        for k in range(j+1,len(s)):
            if s[j] == s[k]:
                if len(s[j+1:k]) > l_max:
                    l_max = len(s[j+1:k])
                    logging.debug(f"match found {l_max}")
    
    l.append(l_max)
    logging.debug(f"l updated {l}")
for k in l:
    print(k)
