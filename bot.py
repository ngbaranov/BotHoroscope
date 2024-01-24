import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import load_config
from handlers import questions, handler_subscription

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot...')

    config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_routers(questions.router, handler_subscription.router)

    # await bot.send_message(chat_id=2052431233, text="Привет")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
