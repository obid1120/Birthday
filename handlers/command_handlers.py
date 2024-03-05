from aiogram import Router, Bot
from aiogram.types import BotCommand, Message
from aiogram.filters import Command
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from config import DB_NAME, BOT_TOKEN
from utils.database import Database
from keyboards.keyboard_handlers import addStaff_kb

command_router = Router()
db = Database(DB_NAME)
bot = Bot(BOT_TOKEN)


@command_router.message(Command('start', prefix='/#!'))
async def start_command_handler(message: Message):
    x = 0
    for tg_id in db.get_tg_id():
        if message.from_user.id == tg_id[0]:
            x += 1
    if x == 0:
        db.add_tg_id(tg_id=message.from_user.id)

    await message.answer(
        text='Assalomu alaykum',
        reply_markup=addStaff_kb
    )

