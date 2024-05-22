from os import path, getenv
import os, time 
#from pyrogram.types import BotCommand

class Config:
    API_ID = int(getenv("API_ID", "29922662"))
    API_HASH = getenv("API_HASH", "fabd9f89368de7cc31357522a0089a56")
    BOT_TOKEN = getenv("BOT_TOKEN", "6752673741:AAEBQf_ZescNZlF_bp6V6b8b_bpuMXXyr0s")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "cv_offical")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1001574664407"))
    ADMIN = list(map(int, getenv("ADMIN", "6047510747").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ironman:ironman@cluster0.o1yjwis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002116542152"))
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/bf2caa1b28d85bfdcd37d.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","AutoRequestAccepterBot")
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4 https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4 https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4 https://telegra.ph/file/293cc10710e57530404f8.mp4 https://telegra.ph/file/506898de518534ff68ba0.mp4 https://telegra.ph/file/dae0156e5f48573f016da.mp4 https://telegra.ph/file/3e2871e714f435d173b9e.mp4 https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4 https://telegra.ph/file/876edfcec678b64eac480.mp4 https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4 https://telegra.ph/file/b4834b434888de522fa49.mp4").split()

    LOGO = """
╔═╗╔╦╗╔═╦╗  ╔══╗╔═╗╔╗─╔╗╔═╗╔╗─╔═╗╔═╗╔═╗╔═╗
║╬║║╔╝║║║║  ╚╗╗║║╦╝║╚╦╝║║╦╝║║─║║║║╬║║╦╝║╬║
║╗╣║╚╗║║║║  ╔╩╝║║╩╗╚╗║╔╝║╩╗║╚╗║║║║╔╝║╩╗║╗╣
╚╩╝╚╩╝╚╩═╝  ╚══╝╚═╝─╚═╝─╚═╝╚═╝╚═╝╚╝─╚═╝╚╩╝
──────────  ──────────────────────────────"""

rkn1 = Config()
