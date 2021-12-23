
import sys
import io
import keyword
import traceback
import asyncio

from getpass import getuser
from os import geteuid
from pyrogram import Client, filters
from EvaMaria.darkprince import telegrapher
