import psycopg2
from config import DB_NAME, DB_PASSWORD, DB_USER, DB_HOST, DB_PORT

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port = DB_PORT
        )

    '''MANAGER ORQALI SQL SAVOLLARNI ISHLATING!'''

    def manager(self, sql, *args,
                fetchone: bool = False,
                fetchall: bool = False,
                fetchmany: bool = False,
                commit: bool = False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                elif fetchone:
                    result = cursor.fetchone()
                elif fetchall:
                    result = cursor.fetchall()
                elif fetchmany:
                    result = cursor.fetchmany()
            return result

    def create_users_table(self):
        sql = """CREATE TABLE IF NOT EXISTS users(
        chat_id BIGINT PRIMARY KEY,
        first_name VARCHAR(100))"""
        self.manager(sql, commit=True)

    def insert_users_table(self, chat_id, first_name):
        sql = """INSERT INTO users(chat_id, first_name) VALUES (%s, %s) ON CONFLICT DO NOTHING"""
        self.manager(sql, chat_id, first_name, commit=True)
    
    def create_chapter_table(self):
        sql = """CREATE TABLE IF NOT EXISTS chapter(
            chapter_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            chapter_name VARCHAR(60) UNIQUE
        )"""
        self.manager(sql, commit=True)

    def create_verse_table(self):
        sql = """CREATE TABLE IF NOT EXISTS verse(
            verse_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            verse_text text,
            chapter_id INTEGER REFERENCES chapter(chapter_id))"""
        self.manager(sql, commit=True)

    def insert_chapter_table(self, chapter_name):
        sql = """INSERT INTO chapter(chapter_name) VALUES (%s) ON CONFLICT DO NOTHING"""
        self.manager(sql, chapter_name, commit=True)

    def insert_verse_teble(self, verse_text, chapter_id):
        sql = """INSERT INTO verse(verse_text, chapter_id) VALUES (%s, %s) ON CONFLICT DO NOTHING"""
        self.manager(sql, verse_text, chapter_id, commit=True)

    def select_chapter_name(self):
        sql = """SELECT chapter_name, chapter_id FROM chapter"""
        return self.manager(sql, fetchall=True)

    def select_chapter_by_paginations(self, offset, limit):
        sql = """SELECT chapter_name, chapter_id FROM chapter
        OFFSET %s
        LIMIT %s"""
        return self.manager(sql, offset, limit, fetchall=True)
    
    def select_count_by_chapter_id( self):
        sql = """SELECT count(chapter_id) FROM chapter"""
        return self.manager(sql, fetchone=True)[0]
    
    def select_chapter_id(self):
        sql = """SELECT chapter_id FROM chapter"""
        return self.manager(sql, fetchall=True)

    def select_count_verse_table(self):
        sql = """SELECT count(verse_id) FROM verse"""
        return self.manager(sql, fetchone=True)[0]

    def select_verse_table(self, chapter_id):
        sql = """SELECT verse_text FROM verse WHERE chapter_id = %s"""
        return self.manager(sql, chapter_id, fetchall=True)