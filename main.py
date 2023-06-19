from aiogram import executor
from config import dp
import logging
from handlers import commands, callback, extra, admin, fsm_anketa


fsm_anketa.register_handlers_fsm_anketa(dp)
commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)
admin.register_handlers_admin(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
executor.start_polling(dp, skip_updates=True)



