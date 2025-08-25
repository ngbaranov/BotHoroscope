from asyncio import run
from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    """
    Загружаем токен бота через переменную окружения
    """
    token: str

@dataclass()
class DBConfig:
    """
    Загружаем данные для подключения к БД
    """
    host: str
    port: int
    user: str
    password: str
    database: str


@dataclass
class Config:
    """
    Загружаем данные из файла .env
    """
    tg_bot: TgBot
    db: DBConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            token=env('TOKEN')
            ),
        db=DBConfig(
            host=env('DB_HOST'),
            port=env.int('DB_PORT'),
            user=env('DB_USER'),
            password=env('DB_PASSWORD'),
            database=env('DB_NAME')
        )
    )

config = load_config()

DB_USER = config.db.user
DB_PASSWORD = config.db.password
DB_HOST = config.db.host
DB_PORT = config.db.port
DB_NAME = config.db.database

async def get_db_url():
    """
    Подключение к БД
    :return:
    """
    return (f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@"
            f"{DB_HOST}:{DB_PORT}/{DB_NAME}")

print(run(get_db_url()))
