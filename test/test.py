import asyncio

import httpx
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


async def fetch_horoscope(zodiac_en="cancer", period="today"):
    # Создаем фейковый User-Agent
    ua = UserAgent()
    headers = {
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': '',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': ua.random,  # Используем фейковый User-Agent
    }

    # Асинхронный HTTP-запрос
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://horo.mail.ru/prediction/{zodiac_en}/{period}/', headers=headers)

    # Парсинг ответа с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    main_content = soup.find('main', itemprop='articleBody')

    # Извлечение текста из найденного элемента, с разделением на строки
    text_lines = main_content.get_text(separator="\n", strip=True)

    # Формирование новых <p> для каждой строки текста
    # paragraphs = ' '.join([f'{line}/n/n'  for line in text_lines])
    # print(paragraphs)
    return text_lines


