import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "5838321"))
API_HASH = os.getenv("API_HASH", "b31649ee8513ccc7f27468389bf1b362")
SESSION = os.getenv("SESSION", "BQBOqNlOEUZlWURs7bENUmslCGLOa18CqIdEfg9mDOPNRKAfGFeqPZb4Lp-x1Bkt31zemSkvDamrs9A3ooZjllLLgm5oKaDi89_owlgKHh-jBvz2fpJsl1J6nxELSl-MrGeuP_oKNk7I_bksPXMVnVoNPXvLGhQ98V9J9Nbyo18_62w-DkO77oDrXSxOjBcWixzfm-spOe45EXSxgEXhwvP1ixtWwjvJ3smzYqnI1UA9icNe1TxU-B-jkzy8TrmCJb8y0izgm76GOT6dOhjn1JEQgtW49urLnOLuwVvK0uOMwovypmzOBJUZfh9KMaKiGHJL6mm44iKT5Ld4euXUPSbUYtbrYwA")
HNDLR = os.getenv("HNDLR", "")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1658252131").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="EvaMaria"))
call_py = PyTgCalls(bot)
