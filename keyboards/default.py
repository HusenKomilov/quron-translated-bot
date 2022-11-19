from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def quran_charter():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton('Qur\'on suralari')
    markup.add(btn)
    
    return markup