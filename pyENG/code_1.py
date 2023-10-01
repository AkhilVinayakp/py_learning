# list 
# splitting a list into equally sized chunks


# %% 
# problem statement.
li = list(range(20))
n = 3
# split the given list into 3 equally sized chucks
# 6 elements in equal split and one with 2 elements on it.

# %%
def splitter(lt: list, splits:int):
    for i in range(0, len(lt), splits):
        yield lt[i:i+n]

# %%
# testing
splitted_data = list(splitter(li, n))
print(splitted_data)
# %%
# without function => using generator expression
splitted_data = (li[i:i+n] for i in range(0, len(li),n))
print(list(splitted_data))

# %%
import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.6f} seconds to execute.")
        return result
    return wrapper
# %%
@measure_time
def gen():
    global li
    global n
    splitted_data = (li[i:i+n] for i in range(0, len(li),n))
    # print(list(splitted_data))/
# %%
gen()
# %%
# splitting with inbuilt functions
from itertools import zip_longest
zipped = zip_longest(li, n)



# %%
