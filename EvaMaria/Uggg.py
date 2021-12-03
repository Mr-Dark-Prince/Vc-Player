from pyrogram import filters
from pyrogram.types import Message

from config import bot as app2
from EvaMaria.utils.filter_groups import autocorrect_group


IS_ENABLED = True


@app2.on_message(
    filters.command(["git"], prefixes=f"{HNDLR}"))
)
async def autocorrect_ubot_toggle(_, message: Message):
    global IS_ENABLED
    if len(message.command) != 2:
        return await message.edit("Not enough arguments.")
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        IS_ENABLED = True
        await message.edit("Enabled!")
    elif state == "disable":
        IS_ENABLED = False
        await message.edit("Disabled!")
    else:
        return await message.edit("Wrong argument, Pass (ENABLE|DISABLE).")


@app2.on_message(
    filters.text & ~filters.edited & filters.user(USERBOT_ID),
    group=autocorrect_group,
)
async def autocorrect_ubot(_, message: Message):
    if not IS_ENABLED:
        return
    text = message.text
    data = await arq.spellcheck(text)
    corrected = data.result.corrected
    if corrected == text:
        return
    await message.edit(corrected)
