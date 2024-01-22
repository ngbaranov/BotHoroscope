from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///users.db", echo=True)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "subscription"
    id: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int]
    name: Mapped[str] = mapped_column(String(30))
    zodiac: Mapped[str] = mapped_column(String(30))


Base.metadata.create_all(engine)


def user_verification(user_id) -> None:
    with Session(bind=engine) as session:
        return session.query(User).filter(User.id_user == user_id).first()


def create_user_subscription(user_id: int, first_name: str, zodiac: str) -> None:
    with Session(engine) as session:
        users = User(
            id_user=user_id,
            name=first_name,
            zodiac=zodiac
        )
        session.add(users)
        session.commit()
