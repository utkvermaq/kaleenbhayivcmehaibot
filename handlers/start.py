from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@itsKaleenBhaiyabot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hei đđģ {}!**\n\nDekh bhai **mai koi devta nhi hu mai bas VC me songs bja sakta hu** Ha lekin kuch features hai **jisse mai aapko Amaze kar sakta hu hue hue!**\n\n**Click /cmdlist For More Help or contact @iamsatyanchal / @SHubHam_XD / @utkarshisop / @dogekapila *".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("â Add To Your Group â", url="http://t.me/itsKaleenBhaiyabot?startgroup=true")
            ],[
            InlineKeyboardButton("đŦ Group", url="https://t.me/heavydriverhaiham"),
            InlineKeyboardButton("đ¤ Contact Owner", url="https://t.me/@PROLABS_127_0_0_1")
            ],[
            InlineKeyboardButton("đ Found error", url="https://t.me/heavydriverhaiham")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@itsKaleenBhaiyabot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**Mai jinda hu itni jaldi thori marunga season 3 aaya ni hai :(**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="đī¸ Owner Group đī¸", url="https://t.me/@PROLABS_127_0_0_1")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@itsKaleenBhaiyabot"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**ā¤ā¤žā¤˛āĨā¤¨ ā¤­āĨā¤¯ā¤ž (Kaleen Bhaiya): Aapki seva me**

__Ã Sabse pahle mujhe apne group me add karo..
Ã Uske bad mujhe admin bna de with all permissions..__

** â Commands**

âĸ `/play` - Song Name : __Plays Via Youtube__
âĸ `/dplay` - Song Name : __Play Via Deezer__
âĸ `/splay` - Song Name : __Play Via Jio Saavn__
âĸ `/playlist` - __Show now playing list__
âĸ `/current` - __Show now playing__

âĸ `/song` - Song Name : __Get The Song From YouTube__
âĸ `/vid` - Video Name : __Get The Video From YouTube__
âĸ `/deezer` - song name : __download songs you want quickly via deezer__
âĸ `/saavn` - song name : __download songs you want quickly via saavn__
âĸ `/search` - YouTube Title : __(Get YouTube Search Query)__

** Commands for group Admins**

âĸ `/skip` : __Skips Music__
âĸ `/pause` : __Pause Playing Music__
âĸ `/resume` : __Resume Playing Music__
âĸ `/end` : __Stops playing Music__
âĸ `/reload` : __Reloads Admin List__
âĸ `/userbotjoin` : __Assistant Joins The Group__
âĸ `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="đī¸ Support Group đī¸", url="https://t.me/@PROLABS_127_0_0_1")
              ]]
          )
      )
