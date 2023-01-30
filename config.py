from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "28649803"))
API_HASH = getenv("API_HASH", "c2905be2a77264f31e96d7cc038a714b")
BOT_TOKEN = getenv("BOT_TOKEN", "5657855915:AAFXVgpxEF5RP_TTFaNhzjNyvfA71AWCxXY")
SESSION_NAME = getenv("SESSION_NAME", "AgBT3HSRox1eq28_qyNeOGznxLpiDXu3_s-62ah80bAG_5y-_QNiz7qY4zjcC7tpI0j5rTbIam2Q0DOeUDXxYw72ygtgIOJqxOnofo7K4u5WKoC-QA615klJY5aVHz72BhB8BX3js0ESsnrSYQyBCjS2nfxm0J71uVI2MJhBPcGnppQ2qHeUk6rPS8lpLJYVhCf6LRWDJPOdOlyX2NuuO-j_vkh3DG4xAPDpeyj6jFul_mjIOh26WQ5S2S1Ndx98a0oBpKNJ5mZ8KH055nxZt7gFLD4hA04IL8bhrQ7oknTK8UsVMqJQ5eLnsGBH6o7tNek7j-PZM-zmlUW4UEDvAHxhAAAAAVu8XDgA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "W_X_I")
ALIVE_NAME = getenv("ALIVE_NAME", "amer")
BOT_USERNAME = getenv("BOT_USERNAME", "RM_1996bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "QDDODD")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "G_Y_3")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5834038328").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5834038328").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
