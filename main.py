from aiogram import Bot, Dispatcher

import asyncio


from config import TOKEN
from handlers import questions


# router: Router = Router()
#
# zodiac_signs = {'Овен': 'aries', 'Телец': 'taurus', 'Близнецы': 'gemini', 'Рак': 'cancer', 'Лев': 'leo',
#                 'Дева': 'virgo', 'Весы': 'libra', 'Скорпион': 'scorpio', 'Стрелец': 'sagittarius',
#                 'Козерог': 'capricorn', 'Водолей': 'aquarius', 'Рыба': 'pisces'}


# def get_zodiac_keyboard(zodiac_signs: dict):
#     keyboard_builder = InlineKeyboardBuilder()
#     for key, value in zodiac_signs.items():
#         keyboard_builder.button(text=key, callback_data=value)
#     keyboard_builder.adjust(3)
#     return keyboard_builder.as_markup()


# @router.message(CommandStart())
# async def start_command(message: Message):
#     await message.answer(text='Привет. Выбери свой знак зодиака:', reply_markup=get_zodiac_keyboard(zodiac_signs))
#
#
# @router.callback_query()
# async def get_horoscope(call: CallbackQuery):
#     await  call.answer()
#     zodiac = call.data
#     zodiac_key = ''.join([key for key, value in zodiac_signs.items() if value == zodiac])+'\n'
#     text =  await get_text_horoscope(zodiac=zodiac)
#     await call.message.edit_text(text=zodiac_key + text, reply_markup=get_zodiac_keyboard(zodiac_signs))


async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(questions.router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())


