Скрипт бота гороскопа.

Написан на aiogram 3, c применением базы данных sqlite 3, взаимодействие с которой
происходит через ORM SQLAlchemy 2.

Бот умеет составлять гороскоп по выбранному знаку зодиака на сегодня, завтра, неделю,
месяц, год.
Реализованна рассылка гороскопа на текущий день, для чего пользователю предлагается
зарегистрироваться. Так же можно отписаться от рассылки.

Скрипт состоит из следующих основных файлов:

bot.py - основной файл, точка входа в проект
.env.example - файл, где реальные секреты заменены на неработающие, но похожие по структуре, 
примеры
.gitignore - файл с исключениями которые не ослеживаются в git
requirements.txt - файл с используемыми библиотеками

config_data - пакет для хранения файлов с конфигурационными данными.
config.py - файл с конфигурационными данными.

database - пакет для работы с базой данных
db - файл, в котором создается бд, проверяется есть ли пользователь в базе, происходит
добавление если пользователя нет.
newsletter - файл выборки из бд для рассылки

fsm - пакет и файл для машины состояний

handlers - Пакет, в котором хранятся обработчики апдейтов.
questions - обработчики гороскопа.
handler_subscription - обработчики подписки.
handler_ubsubscribe - обработчик апдейтов чтобы отписаться от рассылки

keyboards - Пакет с модулями, в которых хранятся и/или динамически 
формируются клавиатуры, отправляемые пользователям ботом, 
в процессе взаимодействия.
keyboard_zodiac - формирование клавиатуры со знаками зодиака и периодами.
keyboard_subscription - вспомогательные клавиатуры: кнопка бургер, работа с рассылкой и т.д.

lexicon - модуль и файл для хранения текстов - ответов бота.

service - модуль для парсинга сайтов и функция отправления рассылки.
get_text_horoscope - парсинг сайтов.
apsched - отправление рассылки.




