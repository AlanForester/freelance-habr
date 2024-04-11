import asyncio
import logging
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from playwright.async_api import async_playwright, Playwright, BrowserContext

load_dotenv()

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6380825405:AAFETDeW9P1Gf7XD7N7_8DGp_B9nGPG5daw")

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    from_id = message.from_user.id
    await message.answer("You " + str(from_id))


async def main():
    await asyncio.gather(dp.start_polling(bot), parser(), return_exceptions=True)


async def parser():
    print("Start parser")
    url = 'https://freelance.habr.com/tasks?categories=development_backend%2Cdevelopment_bots%2Cdevelopment_other%2Cadmin%2Cdevelopment_frontend%2Cdevelopment_scripts%2Ctesting_sites%2Ccontent_specification%2Cmarketing_sales%2Cmarketing_research%2Cother_audit_analytics'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    articles = soup.findAll('article')
    for article in articles:
        title_element = article.find("div", class_="task__title")
        print(title_element.text)


if __name__ == "__main__":
    asyncio.run(main())
