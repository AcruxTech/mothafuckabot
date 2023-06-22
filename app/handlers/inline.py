from aiogram import Dispatcher, types

from app.services.flow import Flow
from app.services.palindrome import Palindrome
from app.services.misc_functions import to_fence_font


async def inline_handler(query: types.InlineQuery):
    p = Palindrome()
    f = Flow()
    if query.query:
        response = [
            # БаЛьШиЕ и МаЛеНьКиЕ БуКаФфКи ДаЛжНЫ ЧерЕдАвАцЦо, ЧмЯФфК
            types.InlineQueryResultArticle(
                id=0,
                title='Шрифт заборчиком',
                input_message_content=types.InputTextMessageContent(
                    message_text=to_fence_font(query.query),
                )
            ),
            types.InlineQueryResultArticle(
                id=1,
                title='Shrug эмодзи',
                input_message_content=types.InputTextMessageContent(
                    message_text=f'{query.query} ¯\_(ツ)_/¯',
                )
            ),
        ]
    else:
        response = [
            types.InlineQueryResultArticle(
                id=0,
                title='Палиндромы',
                input_message_content=types.InputTextMessageContent(
                    message_text=f'Ближайший полин гном: <b>{p.get_next().strftime("%H:%M")}</b>\nДо него осталось <b>{p.get_time_to_next()}</b>',
                    parse_mode='HTML'
                )
            ),
            types.InlineQueryResultArticle(
                id=1,
                title='Потоки',
                input_message_content=types.InputTextMessageContent(
                    message_text=f'Ближайший поток: <b>{f.get_next().strftime("%H:%M")}</b>\nДо него осталось <b>{f.get_time_to_next()}</b>',
                    parse_mode='HTML'
                )
            ),
        ]
    await query.answer(response, is_personal=True, cache_time=10)


def register_inline_handlers(dp: Dispatcher):
    dp.register_inline_handler(inline_handler, state="*")