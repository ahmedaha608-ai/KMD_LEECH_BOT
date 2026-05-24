import os
from pyrogram import Client, filters
from engine import compress_video, download_video
from dotenv import load_dotenv

load_dotenv()
app = Client("KMD_Bot", api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"), bot_token=os.getenv("BOT_TOKEN"))

user_settings = {} # لحفظ الصورة المصغرة لكل مستخدم

@app.on_message(filters.command("leech"))
async def leech_cmd(_, m):
    # كود التحميل مع شريط التقدم
    await m.reply_text("📥 جاري التحميل...")
    # (هنا يوضع كود التحميل باستخدام progress bar)

@app.on_message(filters.command("ytleech"))
async def ytleech_cmd(_, m):
    # جلب الجودات المتاحة للرابط
    await m.reply_text("🔍 جاري فحص الرابط...")

@app.on_message(filters.command("qbimiror"))
async def qb_cmd(_, m):
    # كود إضافة الرابط لبرنامج التورنت
    await m.reply_text("🔗 تم إضافة الرابط إلى قائمة التحميل.")

@app.on_message(filters.command("USERSETTING"))
async def setting_cmd(_, m):
    status = "✅ صورة محفوظة" if m.from_user.id in user_settings else "❌ لا توجد صورة"
    await m.reply_text(f"⚙️ إعداداتك:\n{status}")

app.run()
import os
from pyrogram import Client, filters
from engine import compress_video, download_video
from dotenv import load_dotenv

load_dotenv()
app = Client("KMD_Bot", api_id=os.getenv("API_ID"), api_hash=os.getenv("API_HASH"), bot_token=os.getenv("BOT_TOKEN"))

user_settings = {} # لحفظ الصورة المصغرة لكل مستخدم

@app.on_message(filters.command("leech"))
async def leech_cmd(_, m):
    # كود التحميل مع شريط التقدم
    await m.reply_text("📥 جاري التحميل...")
    # (هنا يوضع كود التحميل باستخدام progress bar)

@app.on_message(filters.command("ytleech"))
async def ytleech_cmd(_, m):
    # جلب الجودات المتاحة للرابط
    await m.reply_text("🔍 جاري فحص الرابط...")

@app.on_message(filters.command("qbimiror"))
async def qb_cmd(_, m):
    # كود إضافة الرابط لبرنامج التورنت
    await m.reply_text("🔗 تم إضافة الرابط إلى قائمة التحميل.")

@app.on_message(filters.command("USERSETTING"))
async def setting_cmd(_, m):
    status = "✅ صورة محفوظة" if m.from_user.id in user_settings else "❌ لا توجد صورة"
    await m.reply_text(f"⚙️ إعداداتك:\n{status}")

app.run()
