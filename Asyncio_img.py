import time
import asyncio
import requests
async def function1():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    print("function 1")

async  def function2():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    print("function 2")

async  def function3():
    URL = "https://instagram.com/favicon.ico"
    response = requests.get(URL)
    open("instagram.ico", "wb").write(response.content)
    print("Function 3")

async def main():
    L = await asyncio.gather(
       function1(),
       function2(),
       function3(),
    )
    print(L)

asyncio.run(main())