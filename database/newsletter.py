from sqlalchemy import select
from sqlalchemy.orm import Session
from database.db import engine


def get_id(User):
    """
    Из базы данных получаем id и знак зодиака, для производства рассылки
    :param User:
    :return:
    """
    with Session(engine) as session:
        stmt = select(User.id_user, User.zodiac)
        return session.execute(stmt)


