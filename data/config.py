from environs import Env

env = Env()

URL = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/all/'
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
