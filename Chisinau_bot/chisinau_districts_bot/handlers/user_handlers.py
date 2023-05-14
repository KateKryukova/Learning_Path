from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from typing import List


# Инициализируем роутер уровня модуля
router: Router = Router()

# # Инициализируем билдер
# kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
#
# # Создаем кнопки
# geo_btn: KeyboardButton = KeyboardButton(
#                                 text='Отправить геолокацию',
#                                 request_location=True)
# buttons: List[KeyboardButton] = [KeyboardButton(
#                                 text=district) for district in ['Ботаника', 'Центр', 'Чеканы', 'Рышкановка', 'Боюканы']]
#
# # Добавляем кнопки в билдер
# #kb_builder.row(, width=1)
# kb_builder.add(geo_btn, *buttons)
# kb_builder.adjust(1, 3)

# Создаем список списков с кнопками
keyboard: List[List[KeyboardButton]] = [
    [KeyboardButton(text=str(i)) for i in range(1, 4)],
    [KeyboardButton(text=str(i)) for i in range(4, 7)]]

keyboard.append([KeyboardButton(text='7')])

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=keyboard,
    resize_keyboard=True)

#Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Выберите район',
                         reply_markup=my_keyboard)

# # Этот хэндлер срабатывает на команду /start
# @router.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text='Выберите район',
#                          reply_markup=kb_builder.as_markup(
#                              resize_keyboard=True,
#                              one_time_keyboard=True))


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
