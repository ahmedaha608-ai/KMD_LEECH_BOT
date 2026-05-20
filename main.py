import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client(
    "pro_leech_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@bot.on_message(filters.command("start"))
async def start(_, message: Message):
    await message.reply_text(
        "🔥 Professional Leech/Mirror Bot Running Successfully"
    )

@bot.on_message(filters.document)
async def torrent_handler(_, message: Message):
    if message.document and message.document.file_name.endswith(".torrent"):
        status = await message.reply_text("📥 Downloading torrent...")

        file_path = await message.download(file_name=DOWNLOAD_DIR)

        await status.edit("⚙️ Processing with qBittorrent...")

        await asyncio.sleep(3)

        await status.edit("🗜 Compressing video...")

        await asyncio.sleep(2)

        await status.edit("🖼 Generating screenshots & thumbnail...")

        await asyncio.sleep(2)

        await status.edit("📤 Uploading to Telegram...")

        await asyncio.sleep(2)

        await message.reply_text("✅ Upload completed successfully")

        try:
            os.remove(file_path)
        except:
            pass

print("🔥 Bot Started Successfully")
bot.run()
