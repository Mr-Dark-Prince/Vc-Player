# © @Mister-Dark-Prince 🍀🌚

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from config import HNDLR


DART_E_MOJI = "🎯"
BOWLING = "🎳"
TRY_YOUR_LUCK = "🎰"
GOAL_E_MOJI = "⚽"
BASKETBALL = "🏀"


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


@Client.on_message(filters.command(["bg", "bowling"], prefixes=f"{HNDLR}"))
async def bowling(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=BOWLING,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


@Client.on_message(filters.command(["luck"], prefixes=f"{HNDLR}"))
async def luck_cownd(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=TRY_YOUR_LUCK,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


@Client.on_message(filters.command(["ball", "fb", "football"], prefixes=f"{HNDLR}"))
async def roll_dice(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=GOAL_E_MOJI,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )


@Client.on_message(filters.command(["basket", "basketball"], prefixes=f"{HNDLR}"))
async def basketball(client, message):
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=BASKETBALL,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
