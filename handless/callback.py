import sqlite3
from keyboards.inline_buttons import questionnary_keyboard
from aiogram import  types,Dispatcher
from config import bot
from DataBase.sql_commands import DataBase



async def start_questionaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Do You Love Python?',
        reply_markup=await questionnary_keyboard()
    )


async def yes_button_call(call: types.CallbackQuery):

    await bot.send_message(
        chat_id=call.from_user.id,
        text='I love too:D',
    )
async def no_button_call(call: types.CallbackQuery):

    await bot.send_message(
        chat_id=call.from_user.id,
        text=':(',
    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionaire_call,
                                       lambda call: call.data == "start questionaire")
    dp.register_callback_query_handler(yes_button_call,
                                       lambda call: call.data == "yup")
    dp.register_callback_query_handler(no_button_call,
                                       lambda call: call.data == "nope")
