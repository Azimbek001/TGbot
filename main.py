from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"Привет {message.from_user.full_name}")
    await message.answer("Введите команду /quiz чтобы сыграть в викторину")
    await message.answer("Введите команду /mem чтобы посмотреть мем года)")

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

@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
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
    )

@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    await message.answer_photo(photo="https://pressa.tv/uploads/posts/2022-02/1646036249_pressa_tv_mem-24.jpeg", caption="Веселый мем!")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def square_handler(message: types.Message):
    if message.text.isdigit():
        number = int(message.text)
        square = number ** 2
        await message.answer(f"Квадрат числа {number}: {square}")
    else:
        await message.answer("Пожалуйста, введите число.")

executor.start_polling(dp, skip_updates=True)

#

