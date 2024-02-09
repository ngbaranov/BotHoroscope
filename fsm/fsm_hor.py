from aiogram.fsm.state import StatesGroup, State


class FSMHor(StatesGroup):
    """
    Машина состояний: знак зодиака, период
    """
    hor_sign = State()
    hor_time = State()
