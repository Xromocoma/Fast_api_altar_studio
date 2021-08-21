import asyncio
import json
import aiofiles


def collect_data():
    tasks = [
        exception_filter(get_data_from_source('data1.json')),
        exception_filter(get_data_from_source('data2.json')),
        exception_filter(get_data_from_source('data3.json'))
    ]
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(asyncio.gather(*tasks))
    temp = []

    for list_data in res:
        for item in list_data:
            temp.append(item)

    return sorted(temp, key=lambda x: x['id'])


async def get_data_from_source(path):
    async with aiofiles.open(f'/home/pahomov/python/Fast-api/app/json_data/{path}') as f:
        data = json.loads(await f.read())
        await f.close()
    return data


async def exception_filter(function):
    try:
        return await asyncio.wait_for(function, timeout=2)
    except:
        return []


print(collect_data())
