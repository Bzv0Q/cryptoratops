import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["text"])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    helpBtn = types.InlineKeyboardButton(text="Help", url="https://t.me/CryptoratopsBot")
    supportBtn = types.InlineKeyboardButton(text="Support", url="https://t.me/Bezv0Q")
    changeBtn = types.InlineKeyboardButton(text="Change", url="https://t.me/CryptoratopsBot")
    sheduleBtn = types.InlineKeyboardButton(text="Shedule", url="https://t.me/CryptoratopsBot")
    infoBtn = types.InlineKeyboardButton(text="Info", url="https://t.me/CryptoratopsBot")
    keyboard.add(helpBtn)
    keyboard.add(supportBtn)
    keyboard.add(changeBtn)
    keyboard.add(sheduleBtn)
    keyboard.add(infoBtn)

    bot.send_message(message.chat.id, "What do you need?", reply_markup=keyboard)

if __name__ == '__main__':
     bot.infinity_polling()