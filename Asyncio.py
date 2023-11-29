import time
import asyncio


async def function1():
    await asyncio.sleep(1)
    print("function 1")
    return "ijaa"

async  def function2():
    await asyncio.sleep(1)
    print("function 2")
    return "ijaxx"

async  def function3():
    await asyncio.sleep(4)
    print("Function 3")
    return "ijaxx ijaa"

async def main():
    L = await asyncio.gather(
       function1(),
       function2(),
       function3(),
    )
    print(L)

asyncio.run(main())