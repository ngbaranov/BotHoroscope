from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.keyboard_subscription  import get_zodiac_subscription, get_start_keyboard
from lexicon.lexicon import LEXICON_ZODIAC_SUBSCRIPTIONS
from database.db import create_user_subscription, user_verification

router: Router = Router()


@router.message(Command("subscription"))
async def get_subscription(message: Message):
    """
    Обработка команды /subscription, проверяем подписан ли пользователь на рассылку, если нет - выбераем знак
    на который подписываться
    """
    if user_verification(message.from_user.id):
        await message.answer(text='Вы уже подписались', reply_markup=get_start_keyboard())
    else:
        await message.answer(text='Подпишитесь на рассылку, выбрав знак или откажитесь выбрав кнопку "Передумать".',
                             reply_markup=get_zodiac_subscription(LEXICON_ZODIAC_SUBSCRIPTIONS))


@router.callback_query(F.data.in_(LEXICON_ZODIAC_SUBSCRIPTIONS.values()))
async def get_period_kb(call: CallbackQuery):
    """
    Добавляем пользователя в базу данных и подписываемся на рассылку
    :param call:
    :return:
    """
    create_user_subscription(call.from_user.id, call.from_user.first_name, call.data)
    await call.message.edit_text(text='Вы успешно подписались', reply_markup=get_start_keyboard())
