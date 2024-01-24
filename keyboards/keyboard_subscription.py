from aiogram.types import InlineKeyboardMarkup, BotCommand, ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardMarkup
from aiogram import Bot

from lexicon.lexicon import LEXICON_ZODIAC_SIGNS, LEXICON_COMMANDS, LEXICON_ZODIAC_SUBSCRIPTIONS


def get_zodiac_subscription(LEXICON_ZODIAC_SUBSCRIPTIONS: dict) -> InlineKeyboardMarkup:
    """
    Из словаря делаем кнопки и возвращаем объект клавиатуры.
    :param LEXICON_ZODIAC_SIGNS:
    """
    keyboard_builder = InlineKeyboardBuilder()
    for key, value in LEXICON_ZODIAC_SUBSCRIPTIONS.items():
        keyboard_builder.button(text=key, callback_data=value)
    keyboard_builder.button(text="Передумать", callback_data="start")
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()


def get_start_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Start", callback_data='start')

    return keyboard_builder.as_markup()


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot) -> None:
    """
    Кнопка-бургер menu для создания рассылки, отказа от рассылки, помощи
    """
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS.items()
    ]
    await bot.set_my_commands(main_menu_commands)
