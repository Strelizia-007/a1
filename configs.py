from os import path, getenv
import os

class Config:
    API_ID = int(getenv("API_ID", "29922662"))
    API_HASH = getenv("API_HASH", "fabd9f89368de7cc31357522a0089a56")
    BOT_TOKEN = getenv("BOT_TOKEN", "6752673741:AAEBQf_ZescNZlF_bp6V6b8b_bpuMXXyr0s")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "CV_Offical")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1001574664407"))
    ADMIN = list(map(int, getenv("ADMIN", "6047510747").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ironman:ironman@cluster0.o1yjwis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002116542152"))
    
    PORT = os.environ.get("PORT", "8080")
    START_PIC = os.environ.get('START_PIC', 'https://telegra.ph/file/bf2caa1b28d85bfdcd37d.jpg')
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/e846f9375e9d4f4975ce4.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","TheStreliziaBot")
    START_MSG = """
🦁𝖧𝖾𝗅𝗅𝗈 {}!
𝖨'𝗆 𝖺𝗇 𝖺𝗎𝗍𝗈 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 [𝖠𝖽𝗆𝗂𝗇 𝖩𝗈𝗂𝗇 𝖱𝖾𝗊𝗎𝖾𝗌𝗍𝗌 ](https://t.me/telegram/153) 𝖠𝖼𝖼𝖾𝗉𝗍𝖾𝗋 𝖡𝗈𝗍.
𝖨 𝖼𝖺𝗇 𝖺𝗉𝗉𝗋𝗈𝗏𝖾 𝗎𝗌𝖾𝗋𝗌 𝗂𝗇 𝖦𝗋𝗈𝗎𝗉𝗌/𝖢𝗁𝖺𝗇𝗇𝖾𝗅𝗌.𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖼𝗁𝖺𝗍 𝖺𝗇𝖽 𝗉𝗋𝗈𝗆𝗈𝗍𝖾 𝗆𝖾 𝗍𝗈 𝖺𝖽𝗆𝗂𝗇 𝗐𝗂𝗍𝗁 𝖺𝖽𝖽 𝗆𝖾𝗆𝖻𝖾𝗋𝗌 𝗉𝖾𝗋𝗆𝗂𝗌𝗌𝗂𝗈𝗇.💭

🔖 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [@Cv_Offical](http://t.me/TheMakiBoT?startgroup=true)
"""
    
rkn1 = Config()
