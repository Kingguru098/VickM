#Don't remove This Line From Here. @Dev_Arora_0981 | @DevArora0981
#Github :- Devarora0981 | Devarora0987
from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re
import asyncio
import time
from datetime import datetime

API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
MONGO_URL = os.environ.get("MONGO_URL", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
OWNER_ID = os.environ.get("OWNER_ID")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
BOT_NAME = os.environ.get("BOT_NAME")
START_IMG1 = os.environ.get("START_IMG1")
START_IMG2 = os.environ.get("START_IMG2", None)
START_IMG3 = os.environ.get("START_IMG3", None)
START_IMG4 = os.environ.get("START_IMG4", None)
START_IMG5 = os.environ.get("START_IMG5", None)
START_IMG6 = os.environ.get("START_IMG6", None)
START_IMG7 = os.environ.get("START_IMG7", None)
START_IMG8 = os.environ.get("START_IMG8", None)
START_IMG9 = os.environ.get("START_IMG9", None)
START_IMG10 = os.environ.get("START_IMG10", None)
STKR = os.environ.get("STKR")
STKR1 = os.environ.get("STKR1", None)
STKR2 = os.environ.get("STKR2", None)
STKR3 = os.environ.get("STKR3", None)
STKR4 = os.environ.get("STKR4", None)
STKR5 = os.environ.get("STKR5", None)
STKR6 = os.environ.get("STKR6", None)
STKR7 = os.environ.get("STKR7", None)
STKR8 = os.environ.get("STKR8", None)
STKR9 = os.environ.get("STKR9", None)

bot = Client(
    "VickBot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


PHOTO = [
    START_IMG1,
    START_IMG2,
    START_IMG3,
    START_IMG4,
    START_IMG5,
    START_IMG6,
    START_IMG7,
    START_IMG8,
    START_IMG9,
    START_IMG10,
]

EMOJIOS = [ 
      "????",
      "????",
      "????",
      "????",
      "???",
      "????",
      "????",
      "????",
      "????",
      "????",
]
      
STICKER = [
      STKR,
      STKR1,
      STKR2,
      STKR3,
      STKR4,
      STKR5,
      STKR6,
      STKR7,
      STKR8,
      STKR9,
]
START = f"""
**??? ???????, ?? ?????? [{BOT_NAME}]({START_IMG1})**
**??? ????? ????? ?????s?????? ???????????????????**
**??????????????????????????????????????????**
**??? ???s???????? /chatbot [?????/???????]**
<b>||??? ??????? ?????????? ???????????????? ??????? ??????????.||</b>
"""
DEV_OP = [
    [
        InlineKeyboardButton(text="???? ????????????? ????", url=f"tg://settings"),
        InlineKeyboardButton(text="??? ???????????????????? ???", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="???? ????????? ?????? ????????? ????",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="???? ?????????? & ?????????s ????", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="?????? s?????????????? ??????", callback_data="SOURCE"),
        InlineKeyboardButton(text="?????? ?????????????? ??????", callback_data="ABOUT"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="???? ????????? ?????? ????????? ????",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="??? s????????????????? ???", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
HELP_READ = f"""
<u>**????????????????????s ??????? {BOT_NAME}**</u>
<u>**???????? ???????????? ?????????????!**</u>
**??????? ???????? ????????????????????s ???????? ????? ???s?????? ??????????:/**
**??????????????????????????????????????????**
<b>||????? @Lucifer_official27||</b>
"""
BACK = [
     [
           InlineKeyboardButton(text="??? ??????????? ???", callback_data="BACK"),
     ],
]

HELP_BTN = [
     [
          InlineKeyboardButton(text="???? ??????s????? ????", callback_data="MUSIC"),
          InlineKeyboardButton(text="???? ??????????????????? ????", callback_data="CHATBOT_CMD"),
     ],
     [
          InlineKeyboardButton(text="???? ???????????s ????", callback_data="TOOLS_DATA"),
          InlineKeyboardButton(text="??? ??????????? ???", callback_data="BACK"),
     ],
]

CHATBOT_ON = [
        [
            InlineKeyboardButton(text="???????????????", callback_data=f"addchat"),
            InlineKeyboardButton(text="?????s??????????", callback_data=f"rmchat"),
        ],
]
TOOLS_DATA_READ = f"""
<u>**???????????s ??????? {BOT_NAME} ????????:**</u>
**??? ???s??? `/repo` ??????? ????????????????? s?????????????? ????????????!**
**??????????????????????????????????????????**
**??? ???s??? `/ping` ??????? ???????????????????? ???????? ????????? ????? {BOT_NAME}**
**??????????????????????????????????????????**
<b>||????? @Lucifer_official27||</b>
"""

CHATBOT_READ = f"""
<u>**????????????????????s ??????? {BOT_NAME}**</u>
**??? ???s??? `/chatbot` ?????? ???????????????/?????s?????????? ???????? ???????????????????.**
**??? ??????????? ??? ???????? ?????????????? ???????????????????? ??????? ??????????????????? ??????????? ???? ????????????? ?????????!!**
**?????????????????????????????????????????????**
<b>||????? @Lucifer_official27||</b>
"""
CHATBOT_BACK = [
        [     
              InlineKeyboardButton(text="??? ??????????? ???", callback_data="CHATBOT_BACK"),
        ],
]

ABOUT_BTN = [
      [
           InlineKeyboardButton(text="???? s????????????????? ????", url=f"https://t.me/{SUPPORT_GRP}"),  
           InlineKeyboardButton(text="???? ?????????? ????", callback_data="HELP"),
      ],
      [    
           InlineKeyboardButton(text="???? ????????????? ????", url=f"https://t.me/{OWNER_USERNAME}"), 
           InlineKeyboardButton(text="?????? s?????????????? ??????", callback_data="SOURCE"),
      ],
      [ 
           InlineKeyboardButton(text="???? ??????????????????s ????", url=f"https://t.me/{UPDATE_CHNL}"),  
           InlineKeyboardButton(text="??? ??????????? ???", callback_data="BACK"),
      ],
]
MUSIC_READ = f"""
**<u>??? ???????, ?? ?????? {BOT_NAME}</u>**
**??? ??? ?????s??? ???????? ????????????????????? ??????s????? ??????????????? ???????? ??????? ????????????????????? ????????????? ?????????????????????????s.**
**??????????????????????????????????????????**
**??? ??????? ????? ????? ????????????????????s ???????? ????s????????? ???? ???????? ????????????????s ???????????? ?????????????.**
**??????????????????????????????????????????**
**??? ??????? ????? ????? ????????????????????s ???????? ????? ???s?????? ?????????? : /**
"""

MUSIC_BTN = [
      [    InlineKeyboardButton(text="?????????????s", callback_data="ADMINS"),
           InlineKeyboardButton(text="???????????", callback_data="AUTH"),
           InlineKeyboardButton(text="??????????", callback_data="PLAY"),
      ],
      [
           InlineKeyboardButton(text="?????????????", callback_data="OWNER"),
           InlineKeyboardButton(text="s?????????", callback_data="SUDO"),
           InlineKeyboardButton(text="???????????s", callback_data="TOOLS"),
      ],
      [
           InlineKeyboardButton(text="???????????", callback_data="BACK_HELP"),
      ],
]

MUSIC_BACK_BTN = [
           [
               InlineKeyboardButton(text="???????????", callback_data="MUSIC_BACK"),
           ],
]
TOOLS_READ = """
<u>**s????????? ???s?????????? ???????????s :**</u>
??? /ping
??? ?????????????? ???? ???????? ??s ????????????? ????? ????????????. [???? ????????????? s????????s ???????? ???????? s??s????????? s?????????s ????? ???????? ????????'s s?????????????.]
??? /start 
??? s???????????s ???????? ????????.
??? /help 
??? s????????s ???????? ???????? ?????????? ??????????? ????? ???????? ????????.
??? /stats
??? s????????s ???????? s??s?????????, ???ss??s???????????, ????????????? ???????? s???????????????? s?????????s ????? ???????? ????????.
??? /sudolist 
??? s????????s ???????? ????s??? ????? s??????????????s.
**????????? ??????? s??????????????s :**
??? /speedtest 
??? ??????????????????? s????????????? s???????????? ???????? ?????????????????? ???????? ?????????.
"""
ADMIN_READ= """
<u>**????????? ?????????????s ???????? ???s??? ????????s??? ????????????????????s :**</u>
??? /pause
??? ?????????s??? ???????? ?????????????????? ???????????????? s??????????????.
??? /resume
??? ?????s???????????? ???????? ?????????s?????? s??????????????.
??? /skip ????? /next
??? s???????? ???????? ?????????????????? ???????????????? s??????????????.
???/end ????? /stop
??? ???????? ???????? ??????????????????? ?????????????? s??????????????."""

AUTH_READ= """
<u>**????????????????????s ?????? ???????????/???????????????? ??????? ???s????? :**</u>
**<u>??????????????????????????? ???s?????s ???????? s????????, ?????????s???, ?????s????????? ???????? ???????? ???????? s?????????????? ??????????????????? ????????????? ???????????s.</u>**
??? /auth [???s???????????????? ????? ???????????? ?????? ??? ???s?????'s ??????ss????????] 
??? ????????? ??? ???s????? ?????? ??????????????????????????? ???s?????s ????s??? ????? ???????? ?????????????.
??? /unauth [???s???????????????? ????? ???????????? ?????? ??? ???s?????'s ??????ss????????] 
??? ?????????????????s ???????? ???s????? ?????????? ??????????????????????????? ???s?????s ????s???.
??? /authusers 
??? s????????s ???????? ????s??? ????? ??????????????????????????? ???s?????s ????? ???????? ?????????????."""

PLAY_READ = """
<u>**????????????????????s ?????? ?????????? s???????s :**</u>
??? /play <s??????? ???????????/????? ???????>
??? s???????????s ???????????????? ???????? ?????????????s????????? s??????? ????? ??????.
??? /queue
??? s????????s ???????? ????s??? ????? ????????????????? ??????????????s ???? ???????? ??????????????.
??? /lyrics [s???????]
??? s????????s ???????? ???????? ???????????s ????? ???????? s??????????????????? s???????.
"""

OWNER_READ = """
<u>**????????????????????s ??????????? ???????? ????????? ????? ???s?????? ???? ????????????? ????? ???????? ???????? :**</u>
??? /chatlist
??? ????s??? ??????? ???????? ???????????s ????????????? ???????? ??s ????????s????????.
??? /clean
??? ????????????? ??????? ???????? ???????????? ??????????????????????????s.
??? /update 
??? ????????????? ??????????????????s ?????????? ???????? ???????????.
??? /maintenance on
??? ??????????????? ???????? ????????????????????????????? ???????????? ????? ???????? ????????.
??? /maintenance off
??? ?????s?????????? ???????? ????????????????????????????? ???????????? ????? ???????? ????????.
???/restart 
??? ?????s???????????s ???????? ???????? ????? ?????????? s?????????????.
"""

SUDO_READ = """
<u>**????????????????????s ??????????? ???????? ????????? ????? ???s?????? ???? s????????? ???s?????s :**</u>
??? /activevc
??? s????????s ???????? ????s??? ????? ????????????????? ?????????????????????????s ????? ????????'s s?????????????.
??? /gban [???s???????????????? ????? ???????????? ?????? ??? ???s?????]
??? ?????????????????? ???????s ??? ???s????? ???? ??????? ???????? s?????????????? ???????????s.
??? /ungban [???s???????????????? ????? ???????????? ?????? ??? ???s?????]
??? ?????????????????? ????????????s ???????? ??-??????????????? ???s?????.
??? /broadcast [??????ss???????? ????? ???????????? ?????? ??? ??????ss????????]
??? ???????????????????s???'s ???????? ???????????? ??????ss???????? ?????? ??????? ???????? s?????????????? ???????????s ????? ???????? ????????.
??? /broadcast_pin [??????ss???????? ????? ???????????? ?????? ??? ??????ss????????]
??? ???????????????????s???'s ???????? ???????????? ??????ss???????? ?????? ??????? ???????? s?????????????? ???????????s ????? ???????? ???????? ???????? ???????'s ???????? ???????????????????s????????? ??????ss????????.
??? /joinassistant [??????????? ???s????????????????/?????]
??? ????????????? ???????? ???ss??s??????????? ?????? ?????????? ??????????? ???????????.
??? /leaveassistant [??????????? ???s????????????????/?????]
??? ????????????? ???????? ???ss??s??????????? ?????? ?????????????? ??????????? ???????????.
??? /leavebot [??????????? ???s????????????????/?????]
??? ????????????? ???????? ???????? ?????? ?????????????? ??????????? ???????????.
??? .approve 
??? ????????????????????s ??? ????????s????? ?????? ?????? ???ss??s???????????. [???????????? ???? ???????!]
??? .disapprove
??? ?????s????????????????????s ??? ????????s????? ???????? ?????? ?????? ???ss??s???????????. [???????????? ???? ???????!]
??? .bio
??? s?????? ??????? ????? ???ss??s???????????. [??????x???!] 
??? .pfp
??? s?????? ???????? ????? ???ss??s???????????. [???????????? ??? ??????????????!]
"""


SOURCE_READ = f"**???????, ???????? s?????????????? ???????????? ????? [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ??s ???????????? ?????????????.**\n**???????????s??? ?????????? ???????? ??????????? & ?????????? ???????? s???????? ???**\n**??????????????????????????????????????????????????????**\n**?????????? ??s ???????? [s?????????????? ????????????](https://github.com/Devarora-0981/Vick)**\n**??????????????????????????????????????????????????????**\n**???? ???????? ??????????? ??????? ?????????????????? ?????????? ???????????????????? ?????? [s????????????????? ???????????](https://t.me/{SUPPORT_GRP}).\n ||????? @Dev_Arora_0981||**"

ABOUT_READ = f"""
**??? [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ??s ????? ????? ?????s?????? ???????????-????????.**
**??? [{BOT_NAME}](https://t.me/{BOT_USERNAME}) ???????????????s ??????????????????????????????????? ?????? ??? ???s?????.**
**??? ??????????s ???????? ???? ?????????????????????????? ?????????? ?????????????s.**
**??? ?????????????????? ???? [???????????????](https://www.python.org) ?????????? [?????????????-?????](https://www.mongodb.com) ???s ??? ?????????????????s???**
**??????????????????????????????????????????**
**??? ????????????? ????? ???????? ????????????????s ???????????? ????????????? ??????? ????????????????? ?????s????? ?????????? ???????? ????????? ?????????????? [{BOT_NAME}](https://t.me/{BOT_USERNAME})**
"""
@bot.on_message(filters.command(["start", "aistart", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    if m.chat.type == "private":
        accha = await m.reply_text(
            text = random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("__???????g ???????g ?????? ??????????????g..__")
        await asyncio.sleep(0.2)
        await accha.edit("__???????g ???????g ??? s????????????g.....__")
        await asyncio.sleep(0.2)
        await accha.edit("__???????g ???????g ?????? s????????????g..__")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
            sticker = random.choice(STICKER),
        )
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo = random.choice(PHOTO),
            caption=f"""**??? ???????, ?? ?????? [{BOT_NAME}](t.me/{BOT_USERNAME})**\n**??? ????? ????? ?????s?????? ???????????????????.**\n**??????????????????????????????????????????**\n**??? ???s???????? /chatbot [?????/???????]**\n<b>||??? ??????? ?????????? ???????????????? ??????? ??????????||</b>""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    else:
        await m.reply_text(
                      text = START,
                      reply_markup = InlineKeyboardMarkup(DEV_OP),
   )

@bot.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    vickdb = MongoClient(MONGO_URL)
    vick = vickdb["VickDb"]["Vick"]
    if query.data == "HELP":
        await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BTN),
                      disable_web_page_preview=True,
     )
    elif query.data == "BACK":
            await query.message.edit(
                  text = START,
                  reply_markup=InlineKeyboardMarkup(DEV_OP),
     )
    elif query.data == "SOURCE":
            await query.message.edit(
                   text = SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,

     )
    elif query.data == "ABOUT":
            await query.message.edit(
                    text = ABOUT_READ,
                    reply_markup = InlineKeyboardMarkup(ABOUT_BTN),
                    disable_web_page_preview=True,
     )
    elif query.data == "MUSIC":
            await query.message.edit(
                    text = MUSIC_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BTN),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(
                    text = MUSIC_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BTN),   
     )
    elif query.data == "ADMINS":
            await query.message.edit(
                    text = ADMIN_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data== "TOOLS_DATA":
            await query.message.edit(
                    text= TOOLS_DATA_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK),
     )
    elif query.data == "MUSIC_BACK":
            await query.message.edit(
                    text = MUSIC_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BTN),
     )
    elif query.data == "BACK_HELP":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN),
     )
    elif query.data == "AUTH":
            await query.message.edit(
                    text = AUTH_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data == "OWNER":
            await query.message.edit(
                    text = OWNER_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data == "PLAY":
            await query.message.edit(
                    text = PLAY_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data == "SUDO":
            await query.message.edit(
                    text = SUDO_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data == "TOOLS":
            await query.message.edit(
                    text = TOOLS_READ,
                    reply_markup = InlineKeyboardMarkup(MUSIC_BACK_BTN), 
     )
    elif query.data == "CHATBOT_CMD":
            await query.message.edit(
                    text = CHATBOT_READ,
                    reply_markup = InlineKeyboardMarkup(CHATBOT_BACK), 
     )
    elif query.data == "CHATBOT_BACK":
            await query.message.edit(
                    text = HELP_READ,
                    reply_markup = InlineKeyboardMarkup(HELP_BTN), 
     )
    elif query.data == "addchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "You don't have permissions to do this baby.",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:           
                await query.edit_message_text(f"**???????????-???????? ?????????????????? ??????????????????.**")
            if is_vick:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**???????????-???????? ?????????????????? ????** {query.from_user.mention}.")
    elif query.data == "rmchat":
        if query.from_user.id not in (await is_admins(query.message.chat.id)):
            return query.answer(
                "**???????? ????????'??? ??????????? ???????????s ?????? ?????? ???????s ?????????!**",
                show_alert=True,
            )
        else:
            is_vick = vick.find_one({"chat_id": query.message.chat.id})
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(f"**???????????-???????? ?????s????????????? ????** {query.from_user.mention}.")
            if is_vick:
                await query.edit_message_text("**???????????-???????? ?????????????????? ?????s?????????????.**")
                            
@bot.on_message(filters.command("repo"))
async def repo(client, message):
    await message.reply_text(
                   text= SOURCE_READ,
                   reply_markup = InlineKeyboardMarkup(BACK),
                   disable_web_page_preview = True,
      )
@bot.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_text(
                        text = HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BTN),
       )

@bot.on_message(filters.command("ping", prefixes=["+", "/", "-", "?", "$", "&"]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "__??????g????g...__"
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("__??????g????g.....__")
        await asyncio.sleep(0.25)
        await txxt.edit_text("__??????g????g...__")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=random.choice(PHOTO),
                             caption=f"??ey ????????!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** ???? al??ve ???? ??nd wor????ng ????ne w?????? a p??ng o??\n??? `{ms}` ms\n\n<b>||????d?? ???????? ?????? ???? [King????](https://t.me/funandtimepass)||</b>",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )


@bot.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"])
    & ~filters.private)
async def chatonoff(client: Client, message: Message):
    if not message.from_user:
        return
    else:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (await is_admins(chat_id)):
            return await message.reply_text(
                "**???????? ????????'????? ????? ?????????????.**"
            )
        else:
            await message.reply_text(
            text="?? <u>**???????????s??? ????? ???????????????? ?????? ???????????????/?????s?????????? ???????????????????.**</u>",
            reply_markup=InlineKeyboardMarkup(CHATBOT_ON),
        )


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vickstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       if not is_vick:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vickdb = MongoClient(MONGO_URL)
       vick = vickdb["VickDb"]["Vick"] 
       is_vick = vick.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_vick:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vickprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")

print(f"{BOT_NAME} ??s ?????????????! ???????? ??????????? ???????! ???????? ????? ?????? @funandtimepass ????????????!!")      
bot.run()
