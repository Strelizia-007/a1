from configs import rkn1
from pyrogram import Client, filters, enums
from pyrogram.errors import UserNotParticipant
from RknDeveloper.untils.database import add_user
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@Client.on_callback_query(filters.regex("rkn_developer"))
async def chk(bot, cb : CallbackQuery):
    try:
        await bot.get_chat_member(rkn1.UPDATECHANNEL_ID, cb.from_user.id)
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("💡 𝘐𝘯𝘧𝘰 💡", callback_data = "about")
                    ],[
                InlineKeyboardButton("𝘜𝘱𝘥𝘢𝘵𝘦𝘴 💭", url="https://t.me/cv_offical"),
                InlineKeyboardButton("🌐 Sᴜᴘᴘᴏʀᴛ", url="http://t.me/TheMakiBoT?startgroup=true")
                ],[
                InlineKeyboardButton("+ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ +", url=f"https://t.me/{rkn1.BOT_USERNAME}?startchannel=Bots4Sale&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("+ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ +", url=f"https://t.me/{rkn1.BOT_USERNAME}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]])            
            add_user(cb.from_user.id)
            await cb.message.edit("🦁𝖧𝖾𝗅𝗅𝗈 {}!\n𝖨'𝗆 𝖺𝗇 𝖺𝗎𝗍𝗈 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 [𝖠𝖽𝗆𝗂𝗇 𝖩𝗈𝗂𝗇 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗌](https://t.me/telegram/153) 𝖠𝖼𝖼𝖾𝗉𝗍𝖾𝗋 𝖡𝗈𝗍.\n𝖨 𝖼𝖺𝗇 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 𝗎𝗌𝖾𝗋𝗌 𝗂𝗇 𝖦𝗋𝗈𝗎𝗉𝗌/𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌.𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍 𝖺𝗇𝖽 𝗉𝗋𝗈𝗆𝗈𝗍𝖾 𝗆𝖾 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 𝗐𝗂𝗍𝗁 𝖺𝖽𝖽 𝗆𝖾𝗆𝖻𝖾𝗋𝗌 𝗉𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇.💭\n\n🔖 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [@Cv_Offical](http://t.me/TheMakiBoT?startgroup=true)**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
            
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer(f"Hey, {cb.from_user.first_name}\nI Lɪᴋᴇ Yᴏᴜʀ Sᴍᴀʀᴛɴᴇss, Bᴜᴛ Dᴏɴ'ᴛ Bᴇ Oᴠᴇʀsᴍᴀʀᴛ! 🤓 \nJᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Fɪʀsᴛ 🥇‌‌", show_alert=True)

#🔥 Please Don't Remove Credit 💳 # ❣️ 
@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
	await update.message.edit_text(
	    #⚠️ don't change source code & source link ⚠️ #
	    text = """<b>» Mʏ Nᴀᴍᴇ: <a href='https://t.me/AutoRequestAccepterBot'>Aᴜᴛᴏ Jᴏɪɴ Rᴇǫᴜᴇsᴛ Bᴏᴛ</a>
‣ Cʀᴇᴀᴛᴏʀ : <a href='tg://settings'>ᴛʜɪs Pᴇʀsᴏɴ</a>
‣ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/starley_tg'>ꜱᴛᴀʀʟᴇʏ</a>
‣ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org'>Pʏʀᴏɢʀᴀᴍ</a>
‣ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'>Pʏᴛʜᴏɴ 3</a>
‣ Dᴀᴛᴀ Bᴀsᴇ : <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a>
‣ Bᴏᴛ Sᴇʀᴠᴇʀ : ‣[Vᴘs]‣<a href='https://app.koyeb.com/'>[Kᴏʏᴇʙ]</a>
‣ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ3.8.3 [sᴛᴀʙʟᴇ]</b>""",
	    reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("+ ᴀᴅᴅ ᴍᴇ +", url="http://t.me/TheHyo_JooBoT?startgroup=true")],[
               InlineKeyboardButton("Bᴀᴄᴋ", callback_data = "rkn_developer")
               ]]
            )
    )
