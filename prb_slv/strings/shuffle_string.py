from typing import List
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(message)s')


class Solution:
    def shuffle(self, string:str, index_arr:List)->str:
        s = list(string)
        logging.debug(s)
        logging.debug(index_arr)
        temp:List = []
        for i in range(len(string)):
            logging.debug(f"{index_arr[i]} and {s[i]} : {s[index_arr[i]]}")
            temp.append(s[index_arr[i]])
        logging.debug(temp)


s = Solution()
s.shuffle("codeleet",
[4,5,6,7,0,1,2,3]
 )