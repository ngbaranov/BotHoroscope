from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message

from services.get_text_horoscope import get_text_horoscope
from keyboards.keyboard_zodiac import get_zodiac_keyboard, kb_zodiac_period
from lexicon.lexicon import LEXICON_ZODIAC_SIGNS, LEXICON_ZODIAC_PERIOD

router: Router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text='Привет. Выбери свой знак зодиака:',
                         reply_markup=get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS))


@router.callback_query(F.data.in_(LEXICON_ZODIAC_SIGNS.values()))
async def get_period_kb(call: CallbackQuery):
    await call.answer()
    global zodiac
    zodiac = call.data
    zodiac_key = ''.join([key for key, value in LEXICON_ZODIAC_SIGNS.items() if value == zodiac]) + '\n'
    text = await get_text_horoscope(zodiac=zodiac)
    await call.message.edit_text(text=zodiac_key + text, reply_markup=kb_zodiac_period(LEXICON_ZODIAC_PERIOD))


@router.callback_query(F.data.in_(LEXICON_ZODIAC_PERIOD.values()))
async def get_period(call: CallbackQuery):
    await call.answer()
    print(call)
    period = call.data
    zodiac_key = ''.join([key for key, value in LEXICON_ZODIAC_SIGNS.items() if value == zodiac]) + '\n'
    zodiac_period = ''.join([key for key, value in LEXICON_ZODIAC_PERIOD.items() if value == period]) + '\n'
    text = await get_text_horoscope(zodiac=zodiac, period=period)
    await call.message.edit_text(text=zodiac_key + zodiac_period + text, reply_markup=kb_zodiac_period(LEXICON_ZODIAC_PERIOD))




@router.callback_query()
async def get_horoscope(call: CallbackQuery):
    await  call.answer()
    zodiac = call.data
    zodiac_key = ''.join([key for key, value in LEXICON_ZODIAC_SIGNS.items() if value == zodiac]) + '\n'
    text = await get_text_horoscope(zodiac=zodiac)
    await call.message.edit_text(text=zodiac_key + text, reply_markup=get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS), )
