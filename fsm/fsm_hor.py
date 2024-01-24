from aiogram.fsm.state import StatesGroup, State


class FSMHor(StatesGroup):
    hor_sign = State()
    hor_time = State()
