# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25588319"))
    API_HASH = getenv("API_HASH", "5972c23e4a53fb0f92d8bec8942833c0")
    BOT_TOKEN = getenv("BOT_TOKEN", "7827847503:AAGCDMvqFdtXonXcu4Lh4OZqqI2XGZykXc4")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "1010979545").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
