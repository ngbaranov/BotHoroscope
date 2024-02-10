from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from services.get_text_horoscope import get_text_horoscope
from keyboards.keyboard_zodiac import get_zodiac_keyboard, kb_zodiac_period
from lexicon.lexicon import LEXICON_ZODIAC_SIGNS, LEXICON_ZODIAC_PERIOD, START
from fsm.fsm_hor import FSMHor

router: Router = Router()
storage: MemoryStorage = MemoryStorage()


@router.message(CommandStart(),  StateFilter(default_state))

async def start_command(message: Message, state: FSMContext):
    """
    Обработка команды /start,вход в состояние FSMHor, переход к выбору знака зодиака
    """
    await message.answer(text=START,  reply_markup=get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS))
    await state.set_state(FSMHor.hor_sign)


@router.callback_query(F.data.in_(LEXICON_ZODIAC_SIGNS.values()))
async def get_period_kb(call: CallbackQuery, state: FSMContext):
    """
    Обработка выбора знака зодиака, гороскоп на сегодня по выбранному знаку вызов клавиатуры с периодами гороскопа
    :param call:
    :param state:
    :return:
    """
    await call.answer()
    await state.update_data(hor_sign = call.data)
    zodiac_key = ''.join([key for key, value in LEXICON_ZODIAC_SIGNS.items() if value == call.data]) + '\n'
    text = await get_text_horoscope(zodiac=call.data)
    await call.message.edit_text(text=zodiac_key + text, reply_markup=kb_zodiac_period(LEXICON_ZODIAC_PERIOD))
    await state.set_state(FSMHor.hor_time)


@router.callback_query(F.data.in_(LEXICON_ZODIAC_PERIOD.values()), FSMHor.hor_time)
async def get_period(call: CallbackQuery, state: FSMContext):
    """
    Обработка выбора периода гороскопа, гороскоп по выбранному знаку и периоду
    :param call:
    :param state:
    :return:
    """
    await call.answer()
    await state.update_data(hor_time=call.data)
    horoscope = await state.get_data()
    zodiac_key = (''.join([key for key, value in LEXICON_ZODIAC_SIGNS.items() if value == horoscope['hor_sign']]) +
                  '\n\n')
    zodiac_period = ''.join([key for key, value in LEXICON_ZODIAC_PERIOD.items() if value == call.data]) + '\n\n'
    text = await get_text_horoscope(zodiac=horoscope['hor_sign'], period=call.data)
    await call.message.edit_text(text=zodiac_key + zodiac_period + text,
                                 reply_markup=kb_zodiac_period(LEXICON_ZODIAC_PERIOD))


@router.callback_query(F.data == 'start')
async def start(call: CallbackQuery):
    """
    Переход к выбору знака зодиака
    """
    await call.message.edit_text(text='Выберите знак:',
                                 reply_markup=get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS))

