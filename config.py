from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29426486")
    API_HASH = environ.get("API_HASH", "d71ad4ec048ab41677a1a439b21ff0c9")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://ironman1475767:vijay14757@cluster0.hpz2jjv.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "ironman1475767")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5976437467').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

