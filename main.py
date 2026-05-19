import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not API_ID or not API_HASH or not BOT_TOKEN:
    raise ValueError("Missing environment variables")

bot = Client(
    "leech_bot",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

@bot.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text("Bot is running successfully ✅")

@bot.on_message(filters.document)
async def handle_torrent(_, message: Message):
    if message.document and message.document.file_name.endswith(".torrent"):
        await message.reply_text("Torrent received successfully ⏳")

print("Bot Started...")
bot.run()
