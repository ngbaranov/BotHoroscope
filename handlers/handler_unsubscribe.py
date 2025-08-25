from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from services.db_func import delete_user


from keyboards.keyboard_subscription import get_start_keyboard
from database.db import async_session_maker

Session = async_session_maker()



router: Router = Router()


@router.message(Command("unsubscribe"))
async def get_unsubscribe(message: Message):
    """
    Отписка от рассылки
    :param message:
    :return:
    """
    user_id = message.from_user.id
    await delete_user(user_id)
    await message.answer(text='Вы успешно отписались', reply_markup=get_start_keyboard())
