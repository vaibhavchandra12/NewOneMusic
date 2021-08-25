from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME
from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAELcSphJP9zfZgHUVwbgJr3ctDcwXj2rAACuAcAArHWCFUxMUPx-GRPIiAE")
    await message.reply_text(
        f"""**𝐇𝐞𝐦𝐥𝐨 👋
𝑰 𝒂𝒎 𝑶𝒏𝒆 𝑴𝒖𝒔𝒊𝒄 𝑩𝒐𝒕, 𝑼𝒔𝒆 𝒎𝒆 𝒕𝒐 𝒑𝒍𝒂𝒚 𝒎𝒖𝒔𝒊𝒄 𝒊𝒏 𝒚𝒐𝒖𝒓 𝒈𝒓𝒐𝒖𝒑𝒔 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕.
𝙃𝙤𝙨𝙩𝙚𝙙 𝙊𝙣 𝙑𝙋𝙎, 𝙎𝙤 𝙣𝙤 𝙡𝙖𝙜
𝐎𝐰𝐧𝐞𝐫 - @SherShahxD**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/OneBotsSupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url="https://t.me/OneUpdates"
                    ),
                    InlineKeyboardButton(
                        "🌍 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/friends_ka_adda"
                    )
                ],
                [ 
                    InlineKeyboardButton(
                        "🤔 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", url="https://t.me/OneUpdates/2"
                    )],
                [ 
                    InlineKeyboardButton(
                        "➕ 𝐀𝐝𝐝 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url="https://t.me/OneMusicRoBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**One Music Bot Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/friends_ka_adda")
                ]
            ]
        )
   )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🤔𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩 ?**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/OneBotsSupport")
                ],
                [
                    InlineKeyboardButton(
                        "🤔 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬", url="https://t.me/OneUpdates/2")
                ]
            ]
        )
   )

