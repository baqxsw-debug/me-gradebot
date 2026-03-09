import os
from pyrogram import Client, filters

# وضع البيانات هنا أو عبر متغيرات البيئة
API_ID = int(os.environ.get("API_ID", "20776501"))
API_HASH = os.environ.get("API_HASH", "37dda71d4e738ea345b5a6515e416571")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8256704776:AAF-IHbfh5yzbQdSTUgYTAZbSt2Lrw99Q_g")

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# أمر الفحص
@app.on_message(filters.command("فحص") & filters.private)
async def start(client, message):
    await message.reply("أهلاً بك! السورس يعمل بنجاح وبدون قيود. ✅")

# ميزة الحماية: حذف الروابط في المجموعات
@app.on_message(filters.group & filters.regex(r"t.me|http"))
async def protect(client, message):
    await message.delete()

print("جاري تشغيل السورس...")
app.run()
