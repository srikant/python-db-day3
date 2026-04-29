import asyncio

async def greet(name):

    print(f"Hello, {name}!")
    await asyncio.sleep(1) 
    print(f"Goodbye, {name}!")

asyncio.run(greet("Alice"))    