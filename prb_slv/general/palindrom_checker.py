
'''
check the given number is palindrome
Reading from the left to right as well as left to right gives the same the number.
- Approch
    12321
    1. convert to string and match the string with the given string
    2. with out reversing approch
        - take the values from both the front and back if it is not same then not a palindrome number.

'''
import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

class Solver:
    def __init__(self, number) -> None:
        self.number = number
    def first_take(self):
        nString = str(self.number);
        logging.debug(f"comparing {nString} and {nString[::-1]}");
        return True if(nString == nString[::-1]) else False
    def second_take(self):
        '''
        checking by taking values from the back and front both should be same 
        - conver into a list
        12321
        '''
        nString = list(str(self.number))
        while True:
            try:
                if nString.pop() != nString.pop(0):
                    return False
            except IndexError:
                break
            except Exception as e:
                logging.debug("exiting execution :", e)
                break
        return True
            


if __name__  == "__main__":
    choice = input("enter the choice according to the approach:").strip()
    number = int(input("enter the number to check:"))
    solver = Solver(number)
    match choice:
        case '1':
            try:
                logging.debug(solver.first_take())
            except Exception as e:
                logging.debug("failed to run ", e)
        case '2':
            logging.debug(solver.second_take())
        case _:
            logging.error("please enter a valid choice")


        