# prob
"""
given a string of brackets find out whether they are balanced or not
"""

from stack import DynamicStack, UnderflowException # on dataStruct stack.py
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')


def match(it1: str, it2: str) -> bool:
    if it1 == '{' and it2 == '}':
        return True
    elif it1 == '[' and it2 == ']':
        return True
    elif it1 == '(' and it2 == ')':
        return True
    else:
        return False


def solve(stream: str):
    """stream contains the stream of brackets"""
    #     converting the stream into list
    stream = list(stream)
    logging.debug(f"{stream}")
    #     creating the stack
    stack: DynamicStack = DynamicStack(limit=20)
    #     creating the two list containing the open and closing brackets
    open_br = list("{[(")
    close_br = list("}])")
    is_balanced: bool = True  # keep track the state of balanced
    for i in stream:
        logging.debug(f"{i} from stream")
        if i in open_br:
            stack.push(i)
            logging.debug(f"pushed {i} to the stack \n {stack.show()}")
        elif i in close_br:
            #             pop out the stack if not matches with the current one becomes unbalanced
            try:
                item = stack.pop()
                logging.debug(f" close bracket found {i} pop out element {item}")
            #             check for the match
                if not match(item, i):
                    is_balanced = False
            except UnderflowException:
                is_balanced = False

        else:
            print(f'unknown value found {i}')

    #             printing out the stack
    print(f" stream entered {stream}")
    #     finalizing the result

    if is_balanced and stack.isEmpty():
        print('balanced')
    else:
        print('unbalanced')


if __name__ == '__main__':
    solve("{[]}")
    solve("{{{{]]")


