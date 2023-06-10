from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Контакты')

main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Футболки', callback_data='t-shirt'), 
                 InlineKeyboardButton(text='Шорты', callback_data='shorts'), 
                 InlineKeyboardButton(text='Кроссовки', callback_data='sneakers'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')

contact_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
first_button = KeyboardButton(text=("📱 Отправить"), request_contact=True)
contact_keyboard.add(first_button)

main_keyboard = InlineKeyboardMarkup(row_width=1)
main_keyboard.add(InlineKeyboardButton(text='Записаться', callback_data='new_order'), 
                 InlineKeyboardButton(text='Отменить запись', callback_data='remove_order'), 
                 InlineKeyboardButton(text='Контакты', callback_data='contacts'))