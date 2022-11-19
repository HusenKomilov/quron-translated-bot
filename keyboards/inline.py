from data.loader import bot, db
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def chapter_name_by_paginatsion(page=1):
    markup = InlineKeyboardMarkup()
    page = 1
    limit = 12
    offset = (page-1) * limit

    chapter_all_name = db.select_chapter_by_paginations(offset, limit)

    for item in chapter_all_name:
        # print(item[1])
        markup.add(
            InlineKeyboardButton(f"{item[0]} surasi", callback_data=f'item|{item[1]}'),
        )

    back_to_menu = InlineKeyboardButton('⏮Bosh menyu', callback_data="back_to")

    markup.add(back_to_menu)
    return markup