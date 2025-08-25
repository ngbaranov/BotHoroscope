from tokenize import cookie_re
import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import connection
from models.models import User
from sqlalchemy.orm import Session



@connection
async def user_verification(user_id, session: AsyncSession) -> None:
    """
    Проверка наличия пользователя в базе данных
    :param user_id:
    :return:
    """
    # session.query(User).filter(User.id_user == user_id).first()

    query = select(User).where(User.id_user == user_id)
    result = await session.execute(query)
    return result.scalars().first()

@connection
async def delete_user(user_id, session: AsyncSession ):
    """
    Удаление пользователя из базы данных
    :param user_id:
    :return:
    """
    # session.query(User).filter(User.id_user == user_id).delete()
    query = select(User).where(User.id_user == user_id)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    if user:
        await session.delete(user)
    await session.commit()

@connection
async def create_user_subscription(user_id: int, first_name: str, zodiac: str, session: AsyncSession) -> None:
    """
    Добавляем пользователя в базу данных
    :param user_id:
    :param first_name:
    :param zodiac:
    :return:
    """

    users = User(
        id_user=user_id,
        name=first_name,
        zodiac=zodiac
    )
    session.add(users)
    await session.commit()


@connection
async def get_id(session: AsyncSession):
    """
    Из базы данных получаем id и знак зодиака, для производства рассылки
    :param session:
    :return:
    """

    query = select(User.id_user, User.zodiac)
    result = await session.execute(query)
    return result.all()




