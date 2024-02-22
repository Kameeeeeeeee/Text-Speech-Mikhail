import sqlite3

database = sqlite3.connect("text_to_speech.db")
cursor = database.cursor()

def add_user(message):
    cursor.execute("SELECT tg_id FROM slaves WHERE tg_id=?", (message.chat.id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO slaves (`tg_id`) VALUES (?)", (message.chat.id,))
    database.commit()

# Провайдер
def change_provider(message, provider):
    cursor.execute("SELECT model FROM slaves WHERE tg_id=?", (message.chat.id,))
    cursor.execute("UPDATE slaves SET model = ? WHERE tg_id = ?",(provider.lower(), message.chat.id,))
    database.commit()

def get_provider(message):
    cursor.execute('SELECT model FROM slaves WHERE tg_id=?', (message.chat.id,))
    return cursor.fetchall()[0][0]
# Голос
def change_voice(message, voice):
    cursor.execute("SELECT model FROM slaves WHERE tg_id=?", (message.chat.id,))
    cursor.execute("UPDATE slaves SET voice = ? WHERE tg_id = ?",(voice, message.chat.id,))
    database.commit()

def get_voice(message):
    cursor.execute('SELECT voice FROM slaves WHERE tg_id=?', (message.chat.id,))
    return cursor.fetchall()[0][0].replace('!', '-')

# Попытки
def add_tryes(message, tryes):
    cursor.execute("SELECT tryes FROM slaves WHERE tg_id=?", (message.chat.id,))
    all_tryes = cursor.fetchall()[0][0]
    cursor.execute("UPDATE slaves SET tryes = ? WHERE tg_id = ?",(all_tryes + tryes, message.chat.id,))
    database.commit()

def del_tryes(message, tryes):
    cursor.execute("SELECT tryes FROM slaves WHERE tg_id=?", (message.chat.id,))
    all_tryes = cursor.fetchall()[0][0]
    cursor.execute("UPDATE slaves SET tryes = ? WHERE tg_id = ?",(all_tryes - tryes, message.chat.id,))
    database.commit()

def get_tryes(message):
    cursor.execute("SELECT tryes FROM slaves WHERE tg_id=?", (message.chat.id,))
    return cursor.fetchall()[0][0]