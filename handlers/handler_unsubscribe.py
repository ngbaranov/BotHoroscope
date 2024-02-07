from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database.db import delete_user

from keyboards.keyboard_subscription import get_start_keyboard

router: Router = Router()


@router.message(Command("unsubscribe"))
async def get_unsubscribe(message: Message):
    delete_user(message.from_user.id)
    await message.answer(text='Вы успешно отписались', reply_markup=get_start_keyboard())
