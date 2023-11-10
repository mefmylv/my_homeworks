import sqlite3

from aiogram import  types,Dispatcher
from config import bot
from DataBase.sql_commands import DataBase
from keyboards.inline_buttons import start_keyboard

async def start_button(massage: types.message):
    print(massage)
    db = DataBase()
    try:
        db.sql_insert_users(
            telegram_id=massage.from_user.id,
            username=massage.from_user.username,
            first_name=massage.from_user.first_name,
            last_name=massage.from_user.last_name

    )
    except sqlite3.IntegrityError:
        pass
    await bot.send_message(
        chat_id=massage.from_user.id,
        text=f'Hello {massage.from_user.first_name} {massage.from_user.last_name} ',
        reply_markup=await start_keyboard()

    )
def register_handless(dp:Dispatcher):
    dp.register_message_handler(start_button, commands='start')
