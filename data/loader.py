from telebot import TeleBot
from config import TOKEN
from database.database import DataBase

db = DataBase()

bot = TeleBot(TOKEN, use_class_middlewares=True, parse_mode='html')