from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CgACAgQAAxkBAAIHOmCiPvIVqNf8i2VZGgczCTivaON9AAISAgACVK2MUuB3b1qXOB4eHwQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

✨I can play music in your group's voice chat.
✨ Don't ask for repo else you will be gbanned
✨No support for this musicbot repo.
✨Developed by [ALONE](https://t.me/Tere_bandi_meri_fan_hai).
✨Under development by [Blaze](t.me/piroXpower)

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥Owner🔥", url="t.me/Tere_bandi_meri_fan_hai")
                  ],
                    [
                    InlineKeyboardButton(
                        "🌎Music-world🌎", url="https://t.me/apni_yaari"
                    ),
                    InlineKeyboardButton(
                        "⚡Support⚡", url="https://t.me/patricia_support"
                    )
                ],
                  [ 
                    InlineKeyboardButton(
                        "⚜️ADD ME⚜️", url="https://t.me/TalkzoneXmusicbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/patricia_updates")
                ]
            ]
        )
   )


