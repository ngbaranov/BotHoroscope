import asyncio
import logging

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config_data.config import load_config
from handlers import questions, handler_subscription, handler_unsubscribe, hadler_help
from services.apsched import send_message_cron

logger = logging.getLogger(__name__)


async def main():
    """
    Запуск бота
    """
    # Настройка логирования
    logging.basicConfig(level=logging.DEBUG,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot...')
    # Инициализация бота
    config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    # Рассылка по расписанию
    scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(send_message_cron, 'cron', hour='09', minute='00', args=[bot])
    scheduler.start()
    # Подключение роутеров
    dp.include_routers(questions.router, handler_subscription.router, handler_unsubscribe.router, hadler_help.router)
    #
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
