from aiogram import Bot, Dispatcher, executor, types
from app import keyboards as kb
from app import database as db
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

async def on_startup(_):
    await db.db_start()
    print('Бот запустился!')

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAANBZH4tKmVQrh3fVTnjVBO8lGxVn_AAAj8AA0qOGCYXx_2EukGAMS8E')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в бот!', reply_markup=kb.main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'{message.from_user.first_name}, Вы авторизовались как администратор!', reply_markup=kb.main_admin)

@dp.message_handler(commands=['id'])
async def cmd_id(message: types.Message):
    await message.answer(f'{message.from_user.id}')

@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст', reply_markup=kb.catalog_list)

@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста')

@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Покупать товар у него...')

@dp.message_handler(text='Админ-панель')
async def contacts(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли в админ-панель', reply_markup=kb.admin_panel)
    else:
        await message.reply(f'{message.from_user.first_name}, я тебя не понимаю :(')

@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_message(message.from_user.id, message.chat.id)


@dp.message_handler(content_types=['document', 'photo'])
async def forward_message(message: types.Message):
    await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)


@dp.message_handler()
async def answer(message: types.Message):
    await message.reply(f'{message.from_user.first_name}, я тебя не понимаю :(')

 
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
