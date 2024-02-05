from aiogram import Bot


async def send_message_cron(bpt: Bot):
    await bpt.send_message(chat_id=830117694, text="Bot started!")
