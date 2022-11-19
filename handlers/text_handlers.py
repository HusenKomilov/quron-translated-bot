from telebot.types import Message, ReplyKeyboardRemove
from data.loader import bot, db
from keyboards.inline import chapter_name_by_paginatsion



@bot.message_handler(func=lambda message: message.text == 'Qur\'on suralari')
def quran_suralari(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Sizga kerakli bo'lga qur\'on  surasini tanlang!", reply_markup=ReplyKeyboardRemove())
    bot.send_message(chat_id, 'Qur\'on  suralari', reply_markup=chapter_name_by_paginatsion())

