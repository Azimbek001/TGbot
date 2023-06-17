from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import dp, Dispatcher


@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_2")
    markup.add(next_button)

    quiestion = "Кто старший ментор Backend?"
    answers = [
        "Мирлан",
        "Алтынай",
        "Айдана",
        "Камиля",
        "Омурбек",
    ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать!",
        open_period=5,
        reply_markup=markup
    )


@dp.callback_query_handler(text="next_button_3")
async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_4")
    markup.add(next_button)

    quiestion = "Лучшие курсы программирование?"
    answers = [
        "OGOGO",
        "CODIFY",
        "GEEKS",
        "ITRUN",
        "ITGO",
    ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать!",
        open_period=5,
        reply_markup=markup
    )


async def quiz_4(callback: types.CallbackQuery):
    await callback.message.answer("Это все!")


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")
    dp.register_callback_query_handler(quiz_4, text="next_button_4")
