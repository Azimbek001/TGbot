from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,

)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
share_location = KeyboardButton("share_location", request_location=True)
share_contact = KeyboardButton("share_contact", request_contact=True)

start_markup.add(
    start_button,
    quiz_button,
    share_location,
    share_contact
)