from data.loader import bot, db
from telebot.types import CallbackQuery, ReplyKeyboardRemove
from keyboards.inline import chapter_name_by_paginatsion
from keyboards.default import quran_charter
from pprint import pprint

@bot.callback_query_handler(func=lambda call: call.data == 'back_to')
def back_to(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, '⏮Bosh menyu', reply_markup=quran_charter())


@bot.callback_query_handler(func=lambda call: 'item|' in call.data)
def verse_name(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    chapter_id = call.data.split('|')[1]
    verse = db.select_verse_table(chapter_id)
    bot.send_message(chat_id, 'Siz tanlagan suraning oyatlar tarjimasi.👇')
    vertse_text = [i[0] for i in verse]
    for i in vertse_text:
        bot.send_message(chat_id, f'{i}', reply_markup=quran_charter())
    bot.send_message(chat_id, f"Bu bot test sifatida ishlamoqda.\n Sizda takliflar bo'lsa adminga murojat qiling <a href='https://t.me/huseynkomilov'>Admin</a>")