from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


engine = create_engine(f"sqlite:///./database.db", echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int]
    name: Mapped[str]
    zodiac: Mapped[str]

    def __repr__(self):
        return f'<User(id={self.id_user}, name={self.name}, age={self.zodiac})>'


Base.metadata.create_all(engine)


def user_verification(user_id) -> None:
    with Session(bind=engine) as session:
        return session.query(User).filter(User.id_user == user_id).first()


def delete_user(user_id) -> None:
    with Session(bind=engine) as session:
        session.query(User).filter(User.id_user == user_id).delete()
        session.commit()


def create_user_subscription(user_id: int, first_name: str, zodiac: str) -> None:
    with Session(engine) as session:
        users = User(
            id_user=user_id,
            name=first_name,
            zodiac=zodiac
        )
        session.add(users)
        session.commit()
