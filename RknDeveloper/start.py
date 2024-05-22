#(©) @RknDeveloper ✨


from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant
from RknDeveloper.untils.database import add_user, add_group
from configs import rkn1
import random, asyncio
import os


# Main Process _ _ _ _ _ Users Send Massage 🥀__🥀 Please 😢 Give Credit

@Client.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(bot, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await bot.send_message(
            rkn1.LOG_CHANNEL,
            f"**--#NᴇᴡGʀᴏᴜᴘ @RknDeveloper--**\n\nCʜᴀɴɴᴇʟ & Gʀᴏᴜᴘ Iᴅ: {m.chat.id}\nTɪᴛʟᴇ: `{m.chat.title}`\nUɴ: @{m.chat.username}\n\nBʏ: {m.from_user.mention}"
        )
        await bot.approve_chat_join_request(op.id, kk.id)
        img = random.choice(rkn1.SURPRICE)
        await bot.send_video(kk.id,img, "**🦁𝖧𝖾𝗅𝗅𝗈 {}!\n𝖨'𝗆 𝖺𝗇 𝖺𝗎𝗍𝗈 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 [𝖠𝖽𝗆𝗂𝗇 𝖩𝗈𝗂𝗇 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗌](https://t.me/telegram/153) 𝖠𝖼𝖼𝖾𝗉𝗍𝖾𝗋 𝖡𝗈𝗍.\n𝖨 𝖼𝖺𝗇 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 𝗎𝗌𝖾𝗋𝗌 𝗂𝗇 𝖦𝗋𝗈𝗎𝗉𝗌/𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌.𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍 𝖺𝗇𝖽 𝗉𝗋𝗈𝗆𝗈𝗍𝖾 𝗆𝖾 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 𝗐𝗂𝗍𝗁 𝖺𝖽𝖽 𝗆𝖾𝗆𝖻𝖾𝗋𝗌 𝗉𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇.💭\n\n🔖 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [@Cv_Offical](http://t.me/TheMakiBoT?startgroup=true)**".format(m.from_user.mention, m.chat.title), reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/{rkn1.BOT_USERNAME}?startchannel=Bots4Sale&admin=invite_users+manage_chat")],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/{rkn1.BOT_USERNAME}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                
            ]])            )
        add_user(m.from_user.id)
        await bot.send_message(
            rkn1.LOG_CHANNEL,
            f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {m.from_user.mention}\nIᴅ: `{m.from_user.id}`\nUɴ: @{m.from_user.username}"
            )
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    

# Start Massage _____ # Please 😢 Give Credit 

@Client.on_message(filters.command("start"))
async def op(bot, m :Message):
    try:
        await bot.get_chat_member(rkn1.UPDATECHANNEL_ID, m.from_user.id) 
        if m.chat.type == enums.ChatType.PRIVATE:
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
    
            add_user(m.from_user.id)
            await bot.send_message(
            rkn1.LOG_CHANNEL,
            f"**--Nᴇᴡ Uꜱᴇʀ Sᴛᴀʀᴛᴇᴅ Tʜᴇ Bᴏᴛ--**\n\nUꜱᴇʀ: {m.from_user.mention}\nIᴅ: `{m.from_user.id}`\nUɴ: @{m.from_user.username}"
            )
            await m.reply_photo(photo=rkn1.RKN_PIC, caption="**🦊 Hᴇʟʟᴏ {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @Cv_Offical**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
            
        elif m.chat.type == enums.ChatType.GROUP or enums.ChatType.SUPERGROUP:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Pʀɪᴠᴀᴛᴇ", url="https://t.me/AutoRequestAccepterBot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await bot.send_message(
            rkn1.LOG_CHANNEL,
            f"**--#NᴇᴡGʀᴏᴜᴘ @RknDeveloper--**\n\nCʜᴀɴɴᴇʟ & Gʀᴏᴜᴘ Iᴅ: {m.chat.id}\nTɪᴛʟᴇ: `{m.chat.title}`\nUɴ: @{m.chat.username}\n\nBʏ: {m.from_user.mention}"
            )
            await m.reply_text("**❣️ Hᴇʟʟᴏ {}!\n\nWʀɪᴛᴇ Mᴇ Pʀɪᴠᴀᴛᴇ Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs.**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🥀 Jᴏɪɴ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 🥀", url=f"https://t.me/cv_offical")],[
                    InlineKeyboardButton("𖤍 Tʀʏ Aɢᴀɪɴ ༗", "cv_offical")
                ]
            ]
        )
        await m.reply_text("**💞 Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ!. Iғ Yᴏᴜ Jᴏɪɴᴇᴅ Cʟɪᴄᴋ Tʀʏ Aɢᴀɪɴ Bᴜᴛᴛᴏɴ Tᴏ Cᴏɴғɪʀᴍ. 🥀**".format(rkn1.UPDATE_CHANNEL), reply_markup=key)

