
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys


HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\n• ɪᴀᴍ ᴀ ᴀʟɪᴢᴀ ᴍᴜsɪᴄ ᴘʀᴏᴊᴇᴄᴛ ɪ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴘʀᴏᴊᴇᴄᴛ ʙʏ @Xd_Lif\n• ɪ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ᴠᴄ's\n\n• Hit /help ᴛᴏ ᴋɴᴏᴡ  ᴀʙᴏᴜᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs.</b>"
HELP = """
🎧 <b>ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ's ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ 🤪</b>

🎶 **ᴄᴏᴍᴍᴏɴ ᴄᴏᴍᴍᴀɴᴅs**:
• `/song` __ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍᴇ ʏᴏᴜᴛᴜʙᴇ__
• `/play`  __ᴘʟᴀʏ sᴏɴɢ ʏᴏᴜ ʀᴇǫᴜᴇsᴛᴇᴅ__
• `/help` __sʜᴏᴡ ʜᴇʟᴘ ғᴏʀ ᴄᴏᴍᴍᴀɴᴅs__
• `/dplay` __ᴘʟᴀʏ sᴏɴɢ ʏᴏɪ ʀᴇǫᴜᴇsᴛᴇᴅ ᴠɪᴀ ᴅᴇᴇᴢᴇʀ__
• `splay` __ᴘʟᴀʏ sᴏɴɢ ʏᴏᴜ ʀᴇǫᴜᴇsᴛᴇᴅ ᴠɪᴀ ᴊɪᴏ sᴀᴀᴠɴ__
• `/ytplay` __ᴘʟᴀʏ sᴏɴɢ ᴅɪʀᴇᴄᴛʟʏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ sᴀʀᴠᴇʀ__
• `/search` __sᴇᴀᴇᴄʜ ᴠɪᴅᴇᴏ sᴏɴɢ ʟɪɴᴋs__
• `/current` __sʜᴏᴡ ɴᴏᴡ ᴘʟᴀʏɪɴɢ__
• `/playlist` __sʜᴏᴡ ɴᴏᴡ ᴘʟᴀʏɪɴɢ ʟɪsᴛ__
• `/video` __ᴅᴏᴡɴʟᴏᴀᴅs ᴠɪᴅᴇᴏ sᴏɴɢ ǫᴜɪᴠᴋʟʏ__
🎶 **ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs**:
• `/player`  __ᴏᴘᴇɴ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ sᴇᴛᴛɪɴɢs ᴘᴀɴᴇʟ__
• `/pause` __ᴘᴀᴜsᴇ sᴏɴɢ ᴘʟᴀʏ__
• `/skip` __sᴋɪᴘ ɴᴇxᴛ sᴏɴɢ__
• `/resume`  __ʀᴇsᴜᴍᴇ sᴏɴɢ ᴘʟᴀʏ__
• `/userbotjoin`  __ɪɴᴠɪᴛᴇs ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ__
• `/end` __sᴛᴏᴘ's ᴍᴜsɪᴄ ᴘʟᴀʏ__
• `/admincache` __ʀᴇғʀᴇsʜ ʟɪsᴛ ᴏғ ᴀᴅᴍɪɴs ᴡɪᴛʜ ᴠᴄ ᴘᴏᴡᴇʀ__
© ᴘᴏᴡᴇʀᴇᴅ ʙʏ
[ __@Xd_Lif ⚡ || @aish_jaan_0 ⚡__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('✨ ᴜᴘᴅᴀᴛᴇs', url='https://t.me/MISTY_SUPORT'),
                InlineKeyboardButton('⚡ sᴜᴘᴘᴏʀᴛ', url='https://t.me/MISTY_SUPORTER')
                ],[
                InlineKeyboardButton('🤖 ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Xd_Lif'),
                InlineKeyboardButton('🔥 ᴏᴡɴᴇʀ', url='https://t.me/aish_jaan_0')
                ],[
                InlineKeyboardButton('📜 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📜', url='https://t.me/Xd_Lif'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/6c00f31503c49e1424f3f.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('✨ ᴜᴘᴅᴀᴛᴇs', url='https://t.me/MISTY_SUPORT'),
                InlineKeyboardButton('⚡ sᴜᴘᴘᴏʀᴛ', url='https://t.me/MISTY_SUPORTER')
                ],[
                InlineKeyboardButton('🤖 ᴅᴇᴠᴇʟᴏᴘᴇʀ', url='https://t.me/Xd_Lif'),
                InlineKeyboardButton('🎧 🔥 ᴏᴡɴᴇʀ', url='https://t.me/aish_jaan_0')
                ],[
                InlineKeyboardButton('📜 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📜', url='https://t.me/Xd_Lif'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/6c00f31503c49e1424f3f.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
