import asyncio

from pyrogram import idle

from . import TechQuard
from . import call_py

async def startup():
    # STARTING CLIENTS
    if TechQuard:
        try:
            await sumit.start()
            await sumit.join_chat("vcraidbot")
        except Exception as e:
            print(str(e))


    await vcbot.start()

    if call_py:
        await call_py.start()
    await idle()

loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(startup())
