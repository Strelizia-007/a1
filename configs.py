from os import path, getenv
import os

class Config:
    API_ID = int(getenv("API_ID", "29922662"))
    API_HASH = getenv("API_HASH", "fabd9f89368de7cc31357522a0089a56")
    BOT_TOKEN = getenv("BOT_TOKEN", "6410417594:AAG4GmfMx8UkbgCxypy24OX_Ht-90CR75sc")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "CV_Offical")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1001574664407"))
    ADMIN = list(map(int, getenv("ADMIN", "6047510747").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ironman:ironman@cluster0.o1yjwis.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002116542152"))
    
    PORT = os.environ.get("PORT", "8080")
    RKN_PIC = os.environ.get("RKN_PIC", "https://graph.org/file/e846f9375e9d4f4975ce4.jpg")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","TheStreliziaBot")
    
rkn1 = Config()
