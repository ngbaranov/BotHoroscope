from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, Message


from services.get_text_horoscope import get_text_horoscope
from keyboards.keyboard_zodiac import get_zodiac_keyboard

router:Router = Router()

zodiac_signs = {'Овен': 'aries', 'Телец': 'taurus', 'Близнецы': 'gemini', 'Рак': 'cancer', 'Лев': 'leo',
                'Дева': 'virgo', 'Весы': 'libra', 'Скорпион': 'scorpio', 'Стрелец': 'sagittarius',
                'Козерог': 'capricorn', 'Водолей': 'aquarius', 'Рыба': 'pisces'}


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text='Привет. Выбери свой знак зодиака:', reply_markup=get_zodiac_keyboard(zodiac_signs))


@router.callback_query()
async def get_horoscope(call: CallbackQuery):
    await  call.answer()
    zodiac = call.data
    zodiac_key = ''.join([key for key, value in zodiac_signs.items() if value == zodiac])+'\n'
    text =  await get_text_horoscope(zodiac=zodiac)
    await call.message.edit_text(text=zodiac_key + text, reply_markup=get_zodiac_keyboard(zodiac_signs))