from middlewares import SimpleMiddleware
from data.loader import bot, db
import handlers
from api import chapters, verse
from telebot.types import BotCommand

def create_tables(database, chapters_value, verse_value):
    database.create_users_table()
    database.create_chapter_table()
    database.create_verse_table()

    if database.select_count_by_chapter_id() == 0:
        for chapter_table in chapters_value:
            chapter_id1 = int(chapter_table['id'])
            chapter_name = chapter_table['name_simple']
            database.insert_chapter_table(chapter_name)

            print(chapter_name)

    if database.select_count_verse_table() == 0:
        for verse_table_id in verse_value:
            id = int(verse_table_id['chapter'])

        if id == chapter_id1:
            for insert_verse in verse_value:
                verse_text = insert_verse['text']
                chapter_id = int(insert_verse['chapter'])
                database.insert_verse_teble(verse_text, chapter_id)

bot.set_my_commands(
    commands=[
        BotCommand('/start', "Botni qayta ishga tushirush"),
    ]
)
bot.setup_middleware(SimpleMiddleware(1))

if __name__ == '__main__':
    create_tables(db, chapters, verse)
    bot.infinity_polling()