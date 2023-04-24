from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "10692254"))
API_HASH = getenv("API_HASH", "171b6b2dc3f2874c533212d87503ec06")
BOT_TOKEN = getenv("BOT_TOKEN", "6184763013:AAGIMRghLhCNv7xZBbbONWmmtZbxw8wfFzo")
SESSION_NAME = getenv("SESSION_NAME", "AgAiDTrwEvLUTBQREnm-Ja62r-xiyjZCvj-aosMXiMww1Pp40r2ut2sW7EfBmNiXFZhrW6DKCRI-Y87IsZEqZg0sNA06KNAXQdKBlA0B_ttzZAyG6l27qHX6EU6Y2v3jPpeMawUThcKOtfcIQXr7w7VJdryWQgcNQ7JaI5H0jsdIr6iKm0PV714H_yI5YpX9Hq3FyiK-SwbcHcZyzPlpr9cQcYXsPDOrkJMilx5hmXH_8n_TvJaZtkYd_2VYw59bduJNz4xrOUiaZZrdJI3ShLISXnL0D1fI7vegCSipHSlYGV9C_aDPMlFRgMD38qB5kHlsmEOtvMh2dJPBHzzNe6vfAAAAAUQny1kA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "exRRRx")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "TiGeemusicbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZZ8Z5")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
