from sqlalchemy import select
from sqlalchemy.orm import Session
from db import engine, User


with Session(engine) as session:
    stmt = select(User.name)
    for user in session.scalars(stmt):
        print(user)
