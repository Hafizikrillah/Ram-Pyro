import asyncio
import os
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client as gez
from pyrogram import Client
from geezlibs.ram.helpers.basic import *
from geezlibs.ram.helpers.PyroHelpers import *
from geezlibs.ram.utils.misc import *
from geezlibs.ram.utils.tools import *

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@gez.on_message(filters.command("cp", [".", ",", "?", "!", "*", "$"]) & filters.me)
async def kangcopy(client: Client, message: Message):
    mmk = await message.reply_text("`Processing . . .`")
    link = get_arg(message)
    bot = "Nyolong_lagi_bot"
    if link:
        try:
            await asyncio.sleep(1.5)
            await client.join_chat("userbotch")
            await client.join_chat("b4c0d")
            await client.join_chat("offsideaja")
        except Exception as e:
            return await mmk.edit(message, f"**ERROR:** `{e}`")
        try:
            await asyncio.sleep(1.5)
            tai = await mmk.edit("`Nyolong berhasil...`")
            a = await client.send_message(bot, link)
            await asyncio.sleep(2)
            await a.delete()
            await tai.delete()
            async for c in client.get_chat_history(bot, limit=1):
                await c.copy(message.chat.id)
        except BaseException:
            pass
        try:
            async for f in client.search_messages(message.chat.id, query="Trying to Download."):
                await f.delete()
            async for o in client.search_messages(message.chat.id, query="DOWNLOADING:"):
                await o.delete()
            async for g in client.search_messages(message.chat.id, query="Preparing to Upload!"):
                await g.delete()
        except BaseException:
            pass
