import configparser
import telepot
import time

config = configparser.ConfigParser()
config.read("config.ini")

bot_token = str(config["Telegram"]["bot_token"])
my_chat_id = str(config["Telegram"]["my_chat_id"])


bot = telepot.Bot(bot_token)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == "text":
        my_command = msg["text"]
        if "price" in my_command:
            price = "Bitcoin price = "+ str(prices["BTCUSDT"])
            bot.sendMessage(chat_id, price)

if __name__ == "__main__":
    bot.message_loop(handle)
    while True:
        time.sleep(20)
