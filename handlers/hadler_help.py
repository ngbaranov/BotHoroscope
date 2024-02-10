from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboard_subscription import get_start_keyboard
from lexicon.lexicon import HELP

router: Router = Router()


@router.message(Command("help"))
async def get_unsubscribe(message: Message):
    """
    Отписка от рассылки
    :param message:
    :return:
    """
    await message.answer(text=HELP, reply_markup=get_start_keyboard())