from os import environ as env


class Config:
    TELEGRAM_BOT_TOKEN = env["TELEGRAM_BOT_TOKEN"] or ""


CONF = Config()
