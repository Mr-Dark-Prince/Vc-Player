from io import BytesIO
from traceback import format_exc

import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from Python_ARQ import ARQ

from config import HNDLR
from EvaMaria.helpers.merrors import capture_err

ARQ_API_KEY = "LXUNEZ-ZCANAT-AYPGUO-JMORSH-ARQ"
aiohttpsession = aiohttp.ClientSession()
arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)


async def quotify(messages: list):
    response = await arq.quotly(messages)
    if not response.ok:
        return [False, response.result]
    sticker = response.result
    sticker = BytesIO(sticker)
    sticker.name = "sticker.webp"
    return [True, sticker]


def getArg(message: Message) -> str:
    arg = message.text.strip().split(None, 1)[1].strip()
    return arg


def isArgInt(message: Message) -> bool:
    count = getArg(message)
    try:
        count = int(count)
        return [True, count]
    except ValueError:
        return [False, 0]


@Client.on_message(filters.command(["q", "quote"], prefixes=f"{HNDLR}"))
@capture_err
async def quotly_func(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("__🙄Reply To Message To Quote It!__")
    if not message.reply_to_message.text:
        return await message.reply_text(
            "Pesan yang Dibalas tidak memiliki teks apa pun! Tolong Balas Pesan Teks !"
        )
    m = await message.reply_text("`👸Wait....`")
    if len(message.command) < 2:
        messages = [message.reply_to_message]

    elif len(message.command) == 2:
        arg = isArgInt(message)
        if arg[0]:
            if arg[1] < 2 or arg[1] > 10:
                return await m.edit("__Arguments must be between 2-10.__ ")
            count = arg[1]
            messages = await client.get_messages(
                message.chat.id,
                [
                    i
                    for i in range(
                        message.reply_to_message.message_id,
                        message.reply_to_message.message_id + count,
                    )
                ],
                replies=0,
            )
        else:
            if getArg(message) != "r":
                return await m.edit("**SORRY😭**`")
            reply_message = await client.get_messages(
                message.chat.id,
                message.reply_to_message.message_id,
                replies=1,
            )
            messages = [reply_message]
    else:
        await m.edit("**🌚ERROR**")
        return
    try:
        sticker = await quotify(messages)
        if not sticker[0]:
            await message.reply_text(sticker[1])
            return await m.delete()
        sticker = sticker[1]
        await message.reply_sticker(sticker)
        await m.delete()
        sticker.close()
    except Exception as e:
        await m.edit(
            " 🌚Something went wrong..🏃‍♀️"
        )
        e = format_exc()
        print(e)
