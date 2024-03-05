from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from states.states import AddStaffStates
from config import DB_NAME
from utils.database import Database

message_router = Router()
db = Database(DB_NAME)


@message_router.message(F.text == 'Add staff')
async def add_staff_handler(message: Message, state: FSMContext):
    await state.set_state(AddStaffStates.firstnameState)
    await message.answer(
        text='PLease, send firstname: '
    )


@message_router.message(AddStaffStates.firstnameState)
async def add_staff_handler(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(firstname=message.text)
        await state.set_state(AddStaffStates.lastnameState)
        await message.answer(
            text='PLease, send lastname:'
        )
    else:
        await message.answer(text="Please, send text")


@message_router.message(AddStaffStates.lastnameState)
async def add_staff_handler(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(lastname=message.text)
        await state.set_state(AddStaffStates.imageState)
        await message.answer(
            text='PLease, send image: '
        )
    else:
        await message.answer(text="Please, send text")


@message_router.message(AddStaffStates.imageState)
async def add_staff_handler(message: Message, state: FSMContext):
    if message.photo:
        await state.update_data(photo=message.photo[-1].file_id)
        await state.set_state(AddStaffStates.positionState)
        await message.answer(
            text='PLease, send position:'
        )
    else:
        await message.answer(text="Please, send photo")


@message_router.message(AddStaffStates.positionState)
async def position_handler(message: Message, state: FSMContext):
    if message.text:
        await state.set_state(AddStaffStates.birthdayState)
        await state.update_data(position=message.text)
        await message.answer(
            text="Please, send birthday (ex: 20-11-1999):"
        )
    else:
        await message.answer(text="Please, send text")


@message_router.message(AddStaffStates.birthdayState)
async def add_staff_handler(message: Message, state: FSMContext):
    if message.text:
        all_data = await state.get_data()
        firstname = all_data['firstname']
        lastname = all_data['lastname']
        photo = all_data['photo']
        position = all_data['position']
        birthday = message.text

        db.add_staff(
            f_name=firstname,
            l_name=lastname,
            image=photo,
            birthday=birthday,
            position=position
        )
        await message.answer(text="Successfully saved")
    else:
        await message.answer(text="Please, send date")
    await state.clear()