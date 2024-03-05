from aiogram.fsm.state import StatesGroup, State


class AddStaffStates(StatesGroup):
    firstnameState = State()
    lastnameState = State()
    imageState = State()
    birthdayState = State()
    positionState = State()
