from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,

)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
game_button = KeyboardButton("/game")
share_location = KeyboardButton("share_location", request_location=True)
share_contact = KeyboardButton("share_contact", request_contact=True)

start_markup.add(
    start_button,
    quiz_button,
    game_button,
    share_location,
    share_contact
)


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
cancel_button = KeyboardButton("Отмена")
cancel_markup.add(cancel_button)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,

).add(
    KeyboardButton("да"),
    KeyboardButton("заново"),
    cancel_button
)

gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,

).add(
    KeyboardButton("Frontend"),
    KeyboardButton("Backend"),
    KeyboardButton("Android"),
    cancel_button
)

age = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,

).add(
    KeyboardButton("30-1"),
    KeyboardButton("30-2"),
    KeyboardButton("30-3"),
    cancel_button
)

