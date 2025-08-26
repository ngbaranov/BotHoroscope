import datetime

year = str(datetime.datetime.now().year)

LEXICON_ZODIAC_SIGNS: dict = {
    "Овен":      ("aries",       "♈"),
    "Телец":     ("taurus",      "♉"),
    "Близнецы":  ("gemini",      "♊"),
    "Рак":       ("cancer",      "♋"),
    "Лев":       ("leo",         "♌"),
    "Дева":      ("virgo",       "♍"),
    "Весы":      ("libra",       "♎"),
    "Скорпион":  ("scorpio",     "♏"),
    "Стрелец":   ("sagittarius", "♐"),
    "Козерог":   ("capricorn",   "♑"),
    "Водолей":   ("aquarius",    "♒"),
    "Рыба":      ("pisces",      "♓"),
}

LEXICON_ZODIAC_PERIOD: dict = {'Завтра': 'tomorrow', 'Неделя': 'week', 'Месяц': 'month', '2025': 'year'}

LEXICON_COMMANDS: dict = {'/subscription': 'подписаться', '/unsubscribe': 'отписаться', '/help': 'помощь'}

LEXICON_ZODIAC_SUBSCRIPTIONS: dict = {'Овен': 'Aries', 'Телец': 'Taurus', 'Близнецы': 'Gemini', 'Рак': 'Cancer',
                                      'Лев': 'Leo', 'Дева': 'Virgo', 'Весы': 'Libra', 'Скорпион': 'Scorpio',
                                      'Стрелец': 'Sagittarius', 'Козерог': 'Capricorn', 'Водолей': 'Aquarius',
                                      'Рыба': 'Pisces'}

HELP = ('Я бот гороскоп.' + '\n\n' + 'Вот мои команды:' + '\n' + '/help - помощь' + '\n' + '/subscription - подписаться'
        + '\n' + '/unsubscribe - отписаться ' + '\n\n' + 'Я умею составлять гороскопы на день, неделю, месяц или год.')

START = ("Добро пожаловать в гороскоп. " + '\n' + "Я умею составлять гороскопы на день, неделю, месяц или год." + '\n\n'
            + "Чтобы получить гороскоп выберите знак зодиака или войди в меню. ")
