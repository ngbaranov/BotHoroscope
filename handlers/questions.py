from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

# from services.get_text_horoscope import get_text_horoscope
from keyboards.keyboard_zodiac import get_zodiac_keyboard, kb_zodiac_period
from lexicon.lexicon import LEXICON_ZODIAC_SIGNS, LEXICON_ZODIAC_PERIOD, START
from fsm.fsm_hor import FSMHor
from test.test import fetch_horoscope

router: Router = Router()
storage: MemoryStorage = MemoryStorage()

# --- helpers ---------------------------------------------------------------

# Список доступных slug (aries, taurus, ...)
ZODIAC_SLUGS = [slug for slug, _ in LEXICON_ZODIAC_SIGNS.values()]

# slug -> русское название
SLUG_TO_NAME = {slug: (name, emoji) for name, (slug, emoji) in LEXICON_ZODIAC_SIGNS.items()}

# period-значения для фильтра (tomorrow, week, month, 2025)
PERIOD_VALUES = list(LEXICON_ZODIAC_PERIOD.values())


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    """
    Обработка команды /start: показать клавиатуру выбора знака.
    """
    await message.answer(
        text=START,
        reply_markup=get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS),
    )
    await state.set_state(FSMHor.hor_sign)


@router.callback_query(F.data.in_(ZODIAC_SLUGS))
async def get_period_kb(call: CallbackQuery, state: FSMContext):
    """
    Обработка выбора знака: показать гороскоп на сегодня + клавиатуру периодов.
    """
    await call.answer()
    await state.update_data(hor_sign=call.data)

    zodiac_name, emoji = SLUG_TO_NAME.get(call.data, ("Знак", ""))
    text = await fetch_horoscope(zodiac_en=call.data)

    await call.message.edit_text(
        text=f"{emoji} {zodiac_name}\n\n{text}",
        reply_markup=kb_zodiac_period(LEXICON_ZODIAC_PERIOD),
    )
    await state.set_state(FSMHor.hor_time)


@router.callback_query(F.data.in_(PERIOD_VALUES), FSMHor.hor_time)
async def get_period(call: CallbackQuery, state: FSMContext):
    """
    Обработка выбора периода: показать гороскоп по выбранному знаку и периоду.
    """
    await call.answer()

    await state.update_data(hor_time=call.data)
    horoscope = await state.get_data()

    slug = horoscope["hor_sign"]
    zodiac_name, emoji = SLUG_TO_NAME.get(slug, ("Знак", ""))
    period_name = next((k for k, v in LEXICON_ZODIAC_PERIOD.items() if v == call.data), "")

    text = await fetch_horoscope(zodiac_en=slug, period=call.data)

    await call.message.edit_text(
        text=f"{emoji} {zodiac_name}\n\n{period_name}\n\n{text}",
        reply_markup=kb_zodiac_period(LEXICON_ZODIAC_PERIOD),
    )

@router.callback_query(F.data == "start")
async def start(call: CallbackQuery, state: FSMContext):
    """
    Возврат к выбору знака зодиака.
    """
    await call.answer()
    await state.set_state(FSMHor.hor_sign)
    await call.message.edit_text(
        text="Выберите знак:",
        reply_markup=get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS),
    )
