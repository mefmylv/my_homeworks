from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire!",
        callback_data='start questionaire'
    )
    markup.add(questionnaire_button)
    return markup

async def questionnary_keyboard():
    markup = InlineKeyboardMarkup()
    Yes_button = InlineKeyboardButton(
        "Yeah",
        callback_data='yup'
    )
    No_button = InlineKeyboardButton(
        "NO",
        callback_data='nope'
    )
    markup.add(Yes_button)
    markup.add(No_button)
    return markup
