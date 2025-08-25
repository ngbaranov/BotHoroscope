from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base





class User(Base):
    """
    Создаем таблицу в базе данных с id пользователя telegram, его именем и знаком зодиака
    """
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str]
    zodiac: Mapped[str]

    def __repr__(self):
        return f'<User(id={self.id_user}, name={self.name}, age={self.zodiac})>'