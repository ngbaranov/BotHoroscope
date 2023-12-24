from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS: dict):
    keyboard_builder = InlineKeyboardBuilder()
    for key, value in LEXICON_ZODIAC_SIGNS.items():
        keyboard_builder.button(text=key, callback_data=value)
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


def kb_zodiac_period(LEXICON_ZODIAC_PERIOD: dict):
    kb_period_builder = InlineKeyboardBuilder()
    for key, value in LEXICON_ZODIAC_PERIOD.items():
        kb_period_builder.button(text=key, callback_data=value)
    return kb_period_builder.as_markup()
