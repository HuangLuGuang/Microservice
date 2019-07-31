# -*- coding: utf-8 -*-
# @createTime    : 2019/7/26 9:20
# @author  : Huanglg
# @fileName: aiohttp_test.py
# @email: luguang.huang@mabotech.com
import asyncio
import time

from aiohttp import ClientSession

tasks = []
url = "https://www.baidu.com/{}"

async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            print(response)
            print("Hello World:{}".format(time.time()))

def run():
    for i in range(5):
        task = asyncio.ensure_future(hello(url.format(i)))
        tasks.append(task)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))
