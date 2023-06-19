from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from handlers import keyboards


class FSMMentor(StatesGroup):
    name = State()
    age = State()
    direction = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMMentor.name.set()
        await message.answer("Как звать?")
    else:
        await message.reply("Пиши в личке!")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}" \
            if message.from_user.username else None
        data['name'] = message.text
    await FSMMentor.next()
    await message.answer("Скока лет?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    elif not 14 < int(message.text) < 50:
        await message.answer("Доступ воспрещен!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMMentor.next()
        await message.answer("Какое направление?", reply_markup=keyboards.gender_markup )


async def load_direction(message: types.Message, state: FSMContext):

        async with state.proxy() as data:
            data['direction'] = message.text
        await FSMMentor.next()
        await message.answer("Какая группа?", reply_markup=keyboards.age)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text

        name = data['name']
        direction = data['direction']
        age = data['age']
        group = data['group']

        reply_message = (
            f"Имя ментора: {name}\n"
            f"Направление: {direction}\n"
            f"Возраст ментора: {age}\n"
            f"Группа: {group}\n"
        )

    await message.reply(reply_message)
    await FSMMentor.next()
    await message.answer("Все верно?", reply_markup=keyboards.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        await FSMMentor.next()
        await message.answer("Записал в список менторов!")
    elif message.text.lower() == 'заново':
        await FSMMentor.name.set()
        await message.answer("Как звать?")
    else:
        await message.answer("Используй кнопки!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ну и пошел ты!")
    else:
        await message.answer("Что ты отменяешь?!")



def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'], state='*')
    dp.register_message_handler(cancel_reg, Text(equals="отмена", ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMMentor.name)
    dp.register_message_handler(load_age, state=FSMMentor.age)
    dp.register_message_handler(load_direction, state=FSMMentor.direction)
    dp.register_message_handler(load_group, state=FSMMentor.group)
    dp.register_message_handler(submit, state=FSMMentor.submit)
