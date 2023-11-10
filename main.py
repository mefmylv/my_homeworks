from aiogram import  executor
from config import dp
from handless import (
    start,
    callback

)
from DataBase import  sql_commands


async def on_startup(_):
    db = sql_commands.DataBase()
    db.sql_create_tables()

start.register_handless(dp=dp)
callback.register_callback_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup = on_startup
    )

