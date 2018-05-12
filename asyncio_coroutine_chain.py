import asyncio


async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return (result1, result2)


async def phase1():
    return 'result1'


async def phase2(arg):
    print('in phase2')
    return f'result2 derived from {arg}'


event_loop = asyncio.get_event_loop()
try:
    results = event_loop.run_until_complete(outer())
    print(f'The results {results}')
finally:
    event_loop.close()
