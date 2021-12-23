from pyrogram import Client, filters
from config import HNDLR

DART_E_MOJI = "🎯"


@Client.on_message(filters.command(["throw", "dart"], prefixes=f"{HNDLR}"))
async def throw_dart(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DART_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


DICE_E_MOJI = "🎲"


@Client.on_message(filters.command(["dice", "roll"], prefixes=f"{HNDLR}"))
async def roll_dice(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=DICE_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
