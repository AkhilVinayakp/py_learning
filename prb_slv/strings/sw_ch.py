# swapping any two ch of word 2 to test we get the first one

import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s : %(message)s')

class Solution:
    def __init__(self, word_a:str, word_b :str) -> None:
        self.word_a = word_a
        self.word_b = word_b
    
    def bruteforce(self):
        w2 = list(self.word_b)
        logging.debug(f"converting to list {w2}")
        for i in range(len(w2)-1):
            for j in range(i+1, len(w2)):
                # swapping 
                w2[i], w2[j] = w2[j], w2[i]
                logging.debug(f"after swapping the {w2}")
                if ''.join(w2) == self.word_a:
                    return True
                else: 
                    w2[j], w2[i] = w2[i], w2[j]
                    logging.debug(f" reverse swapping {w2}")
        return False
    def check_sim(self):
        w1 = list(self.word_a)
        w2 = list(self.word_b)
        ind = []
        if len(w1) == len(w2):
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    ind.append(i)
            if len(ind) != 2:
                return False
            # now swapping the index
            w2[ind[0]], w2[ind[1]] = w2[ind[1]], w2[ind[0]]
            # after swapping the second list
            logging.debug(f"{w2}")
            if ''.join(w2) == self.word_a:
                return True
        else:
            return False

if __name__ == "__main__":
    s = Solution("ravi","rioa")
    # print(s.bruteforce())
    print(s.check_sim())
