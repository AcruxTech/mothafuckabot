import os
import dotenv

from dataclasses import dataclass


@dataclass
class Bot:
    token: str


@dataclass
class Config:
    tg_bot: Bot


def load_config():
    dotenv.load_dotenv()

    return Config(
        tg_bot=Bot(
            token=os.getenv('BOT_TOKEN')
        )
    )