import requests
import time
from telegram import Bot
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["129897273"]

def get_rate():
    url = "https://api.exchangerate.host/latest?base=EUR&symbols=USD"
    data = requests.get(url).json()
    return data["rates"]["USD"]

bot = Bot(token=TOKEN)

while True:
    rate = get_rate()
    
    if rate >= 1.20:
        bot.send_message(chat_id=CHAT_ID, text=f"🚀 Cambio favorevole: {rate}")
    
    time.sleep(3600)