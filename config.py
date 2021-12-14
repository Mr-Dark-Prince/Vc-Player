import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "17755999"))
API_HASH = os.getenv("API_HASH", "505b6fef2e96f37dabee8e1115af8e63")
SESSION = os.getenv("SESSION", "AQA-F-NhnJx2u26vbLp1KJSVFPMkrEMHudN8BipoUoP__ZXSh76hE-td76yjZ0fTQsF_D6TbN1msD-MedJtPJaoaDk1Vgw-SGv1UEXL3ugcAvn2dsYQDHptRiWM_tww3hLVn_GONjK4ABeoIpnPzoOfMX_ObdFv7c-L67h3Yts51SHbDfz_kNS8_7lsspJ0RgTqJ80m7tpJB__4YdMiL3mz3t4DebHPz-PUt-wUcrAIvb9izeOPq35aq51jKmEv5e-7RV9bi6yQKfCKWCeOM7Snk0jV4Mea3oqnslkcHLnjtsk42ckr9ibOHDU-wpYeMec7K7kCZG6smwn4CpzqDBwpUAAAAASseFXgA")
HNDLR = os.getenv("HNDLR", "")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="EvaMaria"))
call_py = PyTgCalls(bot)
