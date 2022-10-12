import asyncio
import time

async def worker(r_time:float,message: str, name:str)->float:
    st_time = time.perf_counter()
    for _ in  range(6):
        
        await asyncio.sleep(r_time)
        cur_time = time.perf_counter()
        print(f"message from {name} working ongoing {message} for {cur_time-st_time}")
    return cur_time - st_time

async def manager():
    # creating two tasks
    task1 = asyncio.create_task(worker(1, "python","delta"))
    task2 = asyncio.create_task(worker(0.5, "js", "alpha9"))
    # executing something else
    for k in range(6):
        await asyncio.sleep(2)
        print(f"commutting....{k}")
    # waiting for getting the result from the second work
    r_st_2 = await task2
    r_st_1 = await task1
    print("testing ....1")
    print("testing ....2")
    print("testing ....3")
    print("testing ....4")
    # print("total time elapsed for two tasks ",  r_st_2)
    print("total time elapsed for two tasks ", r_st_1 + r_st_2)

asyncio.run(manager())
    

