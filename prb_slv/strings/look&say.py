# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211,
# “Look-and-Say” sequence

from typing import List


class L_and_S:
    def next_number(self, n:str)->str:
        out:List = []
        i:int = 0
        while i < len(n):
            count:int = 1
            while i+1 < len(n) and n[i] == n[i+1]:
                count, i = count + 1, i+1
            out.append(str(count)+ n[i])
            i += 1
        return ''.join(out)
    def create_sequence(self, limit = 10):
        n = "1"
        print(n, end=' ')
        for i in range(2, limit+1):
            n = self.next_number(n)
            print(n, end=' ')

        

t = L_and_S()
t.create_sequence()