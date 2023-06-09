import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from app.config.config import load_config 
from app.handlers.common import register_common_handlers
from app.handlers.inline import register_inline_handlers


logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Смотри /help"),
        BotCommand(command="/help", description="Смотри /start"),
        BotCommand(command="/buy_me_coffee", description="Скинь на кофе uwu"),
    ]
    await bot.set_my_commands(commands)


async def main():
    # Удаляем старые логи, если они есть
    if(os.path.isfile('bot.log')):
        os.remove('bot.log')

    # Настройка логирования в stdout
    logging.basicConfig(
        filename="bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.info("Starting bot")

    # Объявление и инициализация объектов бота и диспетчера
    bot = Bot(token=load_config().tg_bot.token)
    print((await bot.get_me()).username)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    # Регистрация хэндлеров
    register_common_handlers(dp)   
    register_inline_handlers(dp)  

    # Установка команд бота     
    await set_commands(bot) 

    # Запуск поллинга                    
    await dp.start_polling()                    


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass