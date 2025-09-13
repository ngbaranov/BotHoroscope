from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    """
    Функция для настройки кнопки Menu бота
    """
    main_menu_commands = [
        BotCommand(command='/start', description='Запустить бота'),
        BotCommand(command='/help', description='Справка по работе бота'),
        BotCommand(command='/subscribe', description='Подписаться на рассылку'),
        BotCommand(command='/unsubscribe', description='Отписаться от рассылки'),
    ]
    await bot.set_my_commands(main_menu_commands)