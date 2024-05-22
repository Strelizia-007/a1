from pyrogram.types import BotCommand


# Commond Automatic Set 📐
#(©) @RknDeveloper Repo - https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot 
# Please Don't Remove Credit 🙏
async def set_commands(app):
    RKN = [
        BotCommand("start", "Check Bot Alive."),
        BotCommand("users", "Total Users Check.(Aᴅᴍɪɴ Oɴʟʏ)"),
        BotCommand("broadcast", "Broadcast Message Send All Users In Bot (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("fd_broadcast", "Broadcast Message with Forward Tag (Aᴅᴍɪɴ Oɴʟʏ)."),
        BotCommand("restart", "Restarts or re-deploys the server (Aᴅᴍɪɴ Oɴʟʏ).")
 
    ]
    await app.set_bot_commands(RKN)
  
