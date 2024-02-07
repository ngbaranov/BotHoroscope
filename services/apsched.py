from aiogram import Bot

from database.db import User
from database.newsletter import get_id
from services.get_text_horoscope import get_text_horoscope


async def send_message_cron(bpt: Bot):
    """
    Отправка рассылки гороскопа на сегодня по знаку зодиака
    :param bpt:
    :return:
    """
    for id_user, zodiac in get_id(User):
        text = zodiac + '\n\n' + await get_text_horoscope(zodiac.lower())

        await bpt.send_message(chat_id=id_user, text=text)

