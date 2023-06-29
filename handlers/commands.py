from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp , Dispatcher
from .keyboards import start_markup
from aiogram.types import ParseMode
from parser2.news import parser


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}",
                           reply_markup=start_markup)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "Сколько учеников в нашей группе?"
    answers = [
        "30",
        "27",
        "22",
        "35",
        "21",
        "нет верного ответа",
    ]

    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать!",
        open_period=5,
        reply_markup=markup
    )


@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    await message.answer_photo(photo="https://pressa.tv/uploads/posts/2022-02/1646036249_pressa_tv_mem-24.jpeg", caption="Веселый мем!")


async def get_news(message: types.Message):
    news_list = parser()
    for i in news_list:
        await message.answer(
            f"{i['link']}\n\n"
            f"<b><a href='{i['link']}'>{i['title']}</a></b>\n"
            f"{i['description']}\n"
            f"{i['date_from_html']}\n",

        )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_news, commands=['news'])


