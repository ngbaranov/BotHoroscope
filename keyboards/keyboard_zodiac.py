from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_zodiac_keyboard(LEXICON_ZODIAC_SIGNS: dict):
    keyboard_builder = InlineKeyboardBuilder()
    for key, value in LEXICON_ZODIAC_SIGNS.items():
        keyboard_builder.button(text=key, callback_data=value)
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


def kb_zodiac_period(LEXICON_ZODIAC_PERIOD: dict):
    kb_period_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []
    for key, value in LEXICON_ZODIAC_PERIOD.items():
        buttons.append(InlineKeyboardButton(text=key, callback_data=value))
    buttons.append(InlineKeyboardButton(text="Сменить знак", callback_data='start'))
    kb_period_builder.row(*buttons, width=4)

    return kb_period_builder.as_markup()
