import asyncio

async def countdown(n):
    for i in range(n,0,-1):
      await asyncio.sleep(1)
      print(i)
      
entered_number  = int(input("enter the number"))
asyncio.run(countdown(entered_number))