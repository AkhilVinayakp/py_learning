import asyncio
import time

def syncMain():
    st_time = time.perf_counter()
    for i in  range(10):
        print(i)
        time.sleep(1)
    print(f"executed in {time.perf_counter() - st_time}")

# syncMain()


# asynchronous

async def asyncMain():
    st_time = time.perf_counter()
    for i in range(10):
        await asyncio.sleep(1)
        print(i)

    print(f"executed in {time.perf_counter() - st_time}")

asyncio.run(asyncMain())