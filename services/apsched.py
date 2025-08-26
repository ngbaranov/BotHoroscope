# services/apsched.py
from aiogram import Bot

from services.db_func import get_id
from test.test import fetch_horoscope
from lexicon.lexicon import LEXICON_ZODIAC_SIGNS, LEXICON_ZODIAC_SUBSCRIPTIONS

# slug -> (Русское имя, emoji)
SLUG_TO_RU = {slug: (ru_name, emoji) for ru_name, (slug, emoji) in LEXICON_ZODIAC_SIGNS.items()}

# Русское имя -> slug
RU_TO_SLUG = {ru_name: slug for ru_name, (slug, _) in LEXICON_ZODIAC_SIGNS.items()}

# English -> slug (через RU_TO_SLUG)
EN_TO_SLUG = {
    en_name: RU_TO_SLUG[ru_name]
    for ru_name, en_name in LEXICON_ZODIAC_SUBSCRIPTIONS.items()
}
EN_TO_SLUG_CF = {en.casefold(): slug for en, slug in EN_TO_SLUG.items()}


def _format_header_and_slug(zodiac_value: str) -> tuple[str, str]:
    """
    Возвращает (заголовок '♓ Рыба', slug 'pisces').
    Поддерживает:
    - slug: 'pisces'
    - русское имя: 'Рыба'
    - английское имя: 'Pisces'
    """
    z = (zodiac_value or "").strip()
    if not z:
        name_ru, emoji = SLUG_TO_RU["aries"]
        return f"{emoji} {name_ru}", "aries"

    zl = z.casefold()

    # slug
    if zl in SLUG_TO_RU:
        name_ru, emoji = SLUG_TO_RU[zl]
        return f"{emoji} {name_ru}", zl

    # English
    if zl in EN_TO_SLUG_CF:
        slug = EN_TO_SLUG_CF[zl]
        name_ru, emoji = SLUG_TO_RU[slug]
        return f"{emoji} {name_ru}", slug

    # Русское имя
    if z in RU_TO_SLUG:
        slug = RU_TO_SLUG[z]
        name_ru, emoji = SLUG_TO_RU[slug]
        return f"{emoji} {name_ru}", slug

    # fallback
    return z, zl


async def send_message_cron(bpt: Bot):
    """
    Рассылка: заголовок '♓ Рыба' + текст гороскопа на сегодня.
    """
    for id_user, zodiac_value in await get_id():
        header, slug = _format_header_and_slug(zodiac_value)
        text = await fetch_horoscope(zodiac_en=slug)
        await bpt.send_message(chat_id=id_user, text=f"{header}\n\n{text}")
