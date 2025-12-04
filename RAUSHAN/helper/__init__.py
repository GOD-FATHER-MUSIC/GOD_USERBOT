import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "lll_GOD_FATHER_PAPA_lll"])

async def join(client):
    try:
        await client.join_chat("GOD_KI_DUNIYA")
    except BaseException:
        pass
