# -*- coding: utf-8 -*-
# @createTime    : 2019/7/25 10:49
# @author  : Huanglg
# @fileName: async_test.py
# @email: luguang.huang@mabotech.com
import time
import asyncio


async def hello():
    # 定义异步函数
    asyncio.sleep(1)
    print("Hello Wrold:{}".format(time.time()))

def run():
    for i in range(5):
        loop.run_until_complete(hello())


loop = asyncio.get_event_loop()

if __name__ == '__main__':
    print("Start:{}".format(time.time()))
    run()
