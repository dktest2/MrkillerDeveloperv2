# Credit @harshil8981.
# Please Don't remove credit.
# Born to make history @harshil8981 !
# Thank you LazyDeveloper for helping us in this Journey
# 🥰  Thank you for giving me credit @harshil8981  🥰
# for any error please contact me -> telegram@Mrkiller_1109 or insta @Mrking_motivational 
# rip paid developers 🤣 - >> No need to buy paid source code while @Mrkiller_1109 is here 😍😍
import asyncio
import logging
import aiohttp
import traceback
from info import *


async def ping_server():
    sleep_time = PING_INTERVAL
    while True:
        await asyncio.sleep(sleep_time)
        try:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=10)
            ) as session:
                async with session.get(URL) as resp:
                    logging.info("Pinged server with response: {}".format(resp.status))
        except TimeoutError:
            logging.warning("Couldn't connect to the site URL..!")
        except Exception:
            traceback.print_exc()
