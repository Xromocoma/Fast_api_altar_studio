import asyncio
import json
import aiofiles
from app.config import settings

async def collect_data():
    tasks = [
         exception_filter(get_data_from_source('data1.json')),
         exception_filter(get_data_from_source('data2.json')),
         exception_filter(get_data_from_source('data3.json'))
    ]
    res = await asyncio.gather(*tasks)
    temp = []
    for list_data in res:
        for item in list_data:
            temp.append(item)
    return sorted(temp, key=lambda x: x['id'])


async def get_data_from_source(name_file):
    async with aiofiles.open(settings.PATH_TO_SOURCE + name_file) as f:
        data = json.loads(await f.read())
        await f.close()
    return data


async def exception_filter(function):
    try:
        return await asyncio.wait_for(function, timeout=2)
    except:
        return []


