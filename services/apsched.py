from aiogram import Bot

from models.models import User
from services.db_func import get_id
from services.get_text_horoscope import get_text_horoscope
from test.test import fetch_horoscope


async def send_message_cron(bpt: Bot):
    """
    Отправка рассылки гороскопа на сегодня по знаку зодиака
    :param bpt:
    :return:
    """
    for id_user, zodiac in await get_id():
        text = zodiac + '\n\n' + await fetch_horoscope(zodiac.lower())

        await bpt.send_message(chat_id=id_user, text=text)

