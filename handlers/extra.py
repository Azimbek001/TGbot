from aiogram import types
from config import dp, Dispatcher , bot
import random


async def echo_text(message: types.Message) -> None:

    bad_words = ['дурак', 'мал', 'html' , 'дура']
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            await message.delete()
            await message.answer(
                f"Не матерись @{message.from_user.username}\n"
                f"сам ты {word}"
            )

    if message.text.startswith('!pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)
        await message.pin()

    if message.text.startswith('!game'):
        animated_emojis = ['🎯', '🎳', '⚽️', '🏀', '🎰', '🎲']
        random_emoji = random.choice(animated_emojis)
        await message.answer(random_emoji)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_text, content_types=['text'])


# @dp.message_handler(content_types=types.ContentType.TEXT)
# async def square_handler(message: types.Message):
#     if message.text.isdigit():
#         number = int(message.text)
#         square = number ** 2
#         await message.answer(f"Квадрат числа {number}: {square}")
#     else:
#         await message.answer("Пожалуйста, введите число.")

    # dp.register_message_handler(square_handler, content_types=['types.ContentType.TEXT'])

