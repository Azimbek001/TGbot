from aiogram import executor
from config import dp, ADMINs, bot
import logging
from handlers import commands, callback, extra, admin, fsm_anketa


fsm_anketa.register_handlers_fsm_anketa(dp)
commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
extra.register_handlers_extra(dp)


async def on_startup(dp):
    await bot.send_message(ADMINs[0], "Я родился!")



async def on_shutdown(dp):
    await bot.send_message(ADMINs[0], "Пока пока!")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
executor.start_polling(dp, skip_updates=True,
                       on_startup=on_startup,
                       on_shutdown=on_shutdown)



