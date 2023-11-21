import random
import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Yone import dispatcher, pbot, BOT_USERNAME

@pbot.on_message(filters.command(["wall", "wallpaper"]))
async def wall(_, message: Message):
    " ғɪxᴇᴅ ᴡᴀʟʟ ʙʏ am"
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        text = None

    if not text:
        return await message.reply_text("`Please give some query to search.`")

    m = await message.reply_text("`Searching for wallpapers...`")

    try:
        response = requests.get(f"https://api.safone.me/wall?query={text}")
        data = response.json()

        if "results" in data and data["results"]:
            wallpapers = data["results"]
            ran = random.randint(0, min(3, len(wallpapers) - 1))

            await message.reply_photo(
                photo=wallpapers[ran]["imageUrl"],
                caption=f"🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("ʟɪɴᴋ", url=wallpapers[ran]["imageUrl"])],
                    ]
                ),
            )
            await m.delete()
        else:
            await m.edit_text(f"`Wallpaper not found for: {text}`")

    except Exception as e:
        await m.edit_text(f"`An error occurred: {str(e)}`")

__mod_name__ = "Wall"

__help__ = f"""
@{BOT_USERNAME} ᴄᴀɴ ᴄʀᴇᴀᴛᴇ sᴏᴍᴇ ʙᴇᴀᴜᴛɪғᴜʟ ᴀɴᴅ ᴀᴛᴛʀᴀᴄᴛɪᴠᴇ Wall ғᴏʀ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ᴘɪᴄs.

❍ /wall | /wallpaper (Text) *:* ᴄʀᴇᴀᴛᴇ ᴀ wall ᴏғ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴡɪᴛʜ ʀᴀɴᴅᴏᴍ ᴠɪᴇᴡ.
"""
