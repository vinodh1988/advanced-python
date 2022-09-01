import asyncio
from constants import logging
import time

async def big_task():
    print("Long Task is started may take lot of time to finish")
    await asyncio.sleep(15)
    print('Ran for 15 seconds Task finished')
    logging.info("Task Wrapped @"+time.ctime(time.time()))

async def invokeTask():
    logging.info("Task invoked @"+time.ctime(time.time()))
    await asyncio.gather(big_task())
    logging.info("Done the background task")

def invoke():
    asyncio.run(invokeTask())
