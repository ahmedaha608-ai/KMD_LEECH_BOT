import os
from pyrogram import Client, filters
from engine import download, compress_hevc

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("KMD_V6", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(_, m):
    await m.reply_text("🔥 KMD v6 REAL ENGINE ACTIVE")

@app.on_message(filters.command("leechkmd"))
async def leech(_, m):
    if len(m.command) < 2:
        return await m.reply_text("❌ أرسل الرابط")

    url = m.text.split(None, 1)[1]
    status = await m.reply_text("⏳ Downloading...")

    file = await download(url, "best[height<=720]")

    await status.edit("📤 Uploading video...")
    await m.reply_video(file)

    os.remove(file)

@app.on_message(filters.command("compressorkmd"))
async def compress(_, m):
    if not m.reply_to_message or not m.reply_to_message.video:
        return await m.reply_text("❌ رد على فيديو")

    await m.reply_text("⏳ Processing...")

    file = await m.reply_to_message.download("input.mp4")

    output = compress_hevc("input.mp4")

    await m.reply_video(output)

    os.remove("input.mp4")
    os.remove(output)

app.run()
