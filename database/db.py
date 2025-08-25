from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from config_data.config import get_db_url
import asyncio


DATABASE_URL =   asyncio.run(get_db_url())
# подключаем базу данных
# engine = create_engine(f"sqlite:///./database.db", echo=True)

# Создаем асинхронный движок для работы с базой данных
engine = create_async_engine(url=DATABASE_URL, echo=True)
# Создаем фабрику сессий для взаимодействия с базой данных
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass





# Base.metadata.create_all(engine)


def connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                # Явно не открываем транзакции, так как они уже есть в контексте
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()  # Откатываем сессию при ошибке
                raise e  # Поднимаем исключение дальше
            finally:
                await session.close()  # Закрываем сессию

    return wrapper


