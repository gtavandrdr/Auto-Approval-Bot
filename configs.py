# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "7827847503"))
    API_HASH = getenv("API_HASH", "edf47672dc12ca24509ed2e8b247c726")
    BOT_TOKEN = getenv("BOT_TOKEN", "7827847503:AAGCDMvqFdtXonXcu4Lh4OZqqI2XGZykXc4")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002322725805")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "6016330931").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://akhashalderssss:WdiXao3jkdlVB1Xn@cluster0.sfo2z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
