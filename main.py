import logging
import asyncio
from datetime import datetime

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from config import BOT_TOKEN, DB_NAME
from utils.database import Database
from handlers.command_handlers import command_router
from handlers.message_handler import message_router

bot = Bot(BOT_TOKEN)
db = Database(DB_NAME)


async def birthday():
    day = datetime.now().strftime("%d")
    month = datetime.now().strftime("%m")
    staffs = db.get_staff()
    tg_id = db.get_tg_id()
    print(tg_id)
    for i in tg_id:
        for staff in staffs:
            if day == staff[3][:2] and month == staff[3][3:5]:
                await bot.send_photo(
                    chat_id=int(i[0]),
                    photo=staff[2],
                    caption=f"{staff[0]} {staff[1]}\n\n{staff[3]}\n\nHappy birthday 🎉"
                )


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(birthday, CronTrigger(day_of_week='mon-sun', hour=11, minute=52))
    scheduler.start()

    await bot.set_my_commands(
        commands=[
            BotCommand(command='start', description="Start/restart bot")
        ]
    )

    dispatch = Dispatcher()
    dispatch.include_router(command_router)
    dispatch.include_router(message_router)

    await dispatch.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except:
        print("Bot stopped")
