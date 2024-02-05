from sqlalchemy import select
from sqlalchemy.orm import Session
from database.db import engine, User


def get_id(User):
    with Session(engine) as session:
        stmt = select(User.id_user, User.zodiac)
        return session.execute(stmt)

# with Session(engine) as session:
#     # stmt = select(User.id_user, User.name, User.zodiac)
#     # for i, j, k in session.execute(stmt):
#     #     print(i, j, k)
