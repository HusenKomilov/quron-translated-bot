from data.loader import bot, db
from telebot.types import Message
from keyboards.default import quran_charter

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    db.insert_users_table(chat_id, first_name)
    bot.send_message(chat_id, f"Salom {first_name}", reply_markup=quran_charter())