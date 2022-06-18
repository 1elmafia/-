import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 مرحبا انا بوت يمكنني تشغيل الاغاني في المكالمه
اضغط على زر الاوامر لمعرفة طريقة التشغيل 
تم اصدار هذا البوت من قناة سورس بـــيـــمبو تابعنا هنا [قناة السورس](t.me/UUBU0)...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🐥 اضف البوت 🐥", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        " 🦦 ¦ قناه السورس ", url=f"https://t.me/UUBU0"
                    ),
                    InlineKeyboardButton(
                        "  ☣️ ¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        " 🖥 ¦ الأوامــر ", callback_data="cbcmnds"),
                    InlineKeyboardButton( 
                    ),
                    InlineKeyboardButton(
                        " 🧨 ¦ مطور السورس ", url="https://t.me/O1BOO"
                    )]
            ]
       ),
    )

