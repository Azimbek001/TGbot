import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINs, bot
from apscheduler.triggers.date import DateTrigger


async def special_notification(text):
    for user in ADMINs:
        await bot.send_message(
            chat_id=user,
            text=f"Специальное уведомление: {text}"
        )


async def set_birthday():
    birthday = AsyncIOScheduler(timezone="Asia/Bishkek")
    birthday.add_job(
        special_notification,
        DateTrigger(
            run_date=datetime.datetime(year=2023, month=6, day=30, hour=10, minute=30, second=0)
        ),
        kwargs={"text": "Сегодня особый день!"}
    )

    birthday.start()
