from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext


async def start(message: types.Message):
    await message.answer('Ну привет... Не знаю чем может помочь тебе этот бот, но мне он иногда (точнее, очень редко) пригождается. Может и тебе сгодится.\n\nСмотри /help')


async def help(message: types.Message):
    await message.answer('Пиши в любом чате @mothafuckabot и дальше на интуиции всё должно быть понятно. Если непонятно - сочувствую :\\\n\nВ ближайшем времени планирую сделать пару прикольных штук (шрифт заборчиком и шруг фейс), а дальше посмотрим.\nАдмин живет тут - @aqvalb')


async def coffee(message: types.Message):
    await message.answer('Понравился бот? Знаю, что нет.\n\nСкинь на кофе хотя бы, всё-таки целый вечер на него потратил. Буду благодарен')
    await message.bot.copy_message(message.chat.id, -1001844810557, 2)


def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands="start", state="*")
    dp.register_message_handler(help, commands="help", state="*")
    dp.register_message_handler(coffee, commands="buy_me_coffee", state="*")
