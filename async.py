import asyncio


async def main():
    task1 = asyncio.create_task(fetch_Data())
    task2 = asyncio.create_task(print_numbers())

    val = await task1
    print(val)
    await task2




async def foo(text):
    print(text)
    await asyncio.sleep(1)


async def fetch_Data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data':1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)



asyncio.run(main())

