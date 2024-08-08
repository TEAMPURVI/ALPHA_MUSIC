from RAUSHAN.core.bot import Anony
from RAUSHAN.core.dir import dirr
from RAUSHAN.core.git import git
from RAUSHAN.core.userbot import Userbot
from RAUSHAN.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
YTB = YTM()

