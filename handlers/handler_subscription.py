from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from keyboards.keyboard_subscription  import get_zodiac_subscription, get_start_keyboard
from lexicon.lexicon import LEXICON_ZODIAC_SIGNS, LEXICON_ZODIAC_SUBSCRIPTIONS
from database.db import Base, create_user_subscription, engine, user_verification

router: Router = Router()


@router.message(Command("subscription"))
async def get_subscription(message: Message):
    if user_verification(message.from_user.id):
        await message.answer(text='Вы уже подписались', reply_markup=get_start_keyboard())
    else:
        await message.answer(text='Подпишитесь на рассылку, выбрав знак или откажитесь выбрав кнопку "Передумать".',
                             reply_markup=get_zodiac_subscription(LEXICON_ZODIAC_SUBSCRIPTIONS))


@router.callback_query(F.data.in_(LEXICON_ZODIAC_SUBSCRIPTIONS.values()))
async def get_period_kb(call: CallbackQuery):
    # Base.metadata.create_all(engine)
    # if not db.user_exists(call.from_user.id):
    create_user_subscription(call.from_user.id, call.from_user.first_name, call.data)
    # await call.answer()
    await call.message.edit_text(text='Вы успешно подписались', reply_markup=get_start_keyboard())
    # else:
    #     await call.answer()
    #     await call.message.edit_text(text='Вы уже подписались', reply_markup=get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS))