# using cprofile package
# %%
# imports
import cProfile
import pstats
import time

# %%
def sample_fn():
    total = 0
    for i in range(2,2*1000):
        total += i
    return total
# %%
profiler = cProfile.Profile()
profiler.enable()
sample_fn() # execute the function
profiler.disable()
profiler.print_stats()
# %%
def profile(func):
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(f"{func.__name__}_profile.prof")
        stats = pstats.Stats(f"{func.__name__}_profile.prof")
        stats.strip_dirs().sort_stats('cumulative').print_stats()
        return result
    return wrapper
# %%
@profile
def sample_fn():
    total = 0
    for i in range(2,2*1000):
        total += i
    return total
# %%
sample_fn()
# %%
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
