from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_zodiac_keyboard(zodiac_signs: dict):
    keyboard_builder = InlineKeyboardBuilder()
    for key, value in zodiac_signs.items():
        keyboard_builder.button(text=key, callback_data=value)
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()