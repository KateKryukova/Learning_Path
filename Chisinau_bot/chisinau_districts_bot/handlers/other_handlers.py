import random
from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    try:
        await message.reply(text=random.choice(LEXICON_RU['answers']))
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
