import asyncio
import logging

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler


from config_data.config import load_config
from handlers import questions, handler_subscription
from services.get_text_horoscope import get_text_horoscope
from services.apsched import send_message_cron

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot...')

    config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_message_cron, 'cron', hour='13', minute='10', args=[bot])
    scheduler.start()


    dp.include_routers(questions.router, handler_subscription.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



    # text = await get_text_horoscope('leo', period='today')
    # await bot.send_message(chat_id=830117694, text=text)



if __name__ == '__main__':
    asyncio.run(main())
