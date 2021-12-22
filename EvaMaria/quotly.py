import asyncio
import random
from asyncio import sleep

from pyrogram.types import Message
from pyrogram import Client, filters
from config import HNDLR

@Client.on_message(filters.command(["q"], prefixes=f"{HNDLR}"))
async def quotly(client, m: Message):
    if not m.reply_to_message:
        await m.edit("🙄Reply to any users text message")
        return

    await m.reply_to_message.forward("@QuotLyBot")

    is_sticker = False
    progress = 0

    while not is_sticker:
        try:
            await sleep(4)
            msg = await client.get_history("@QuotLyBot", 1)
            print(msg)
            is_sticker = True
        except:
            await sleep(1)

            progress += random.randint(0, 5)

            if progress > 100:
                await m.reply_text('There was a long running error')
                return

            try:
                await m.edit("```Making a Quote\nProcessing {}%```".format(progress))
            except:
                await m.edit("ERROR")

    if msg_id := msg[0]['message_id']:
        await asyncio.gather(
            m.delete(),
            client.forward_messages(message.chat.id, "@QuotLyBot", msg_id)
        )
