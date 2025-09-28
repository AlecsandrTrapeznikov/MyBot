from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='история')],
    [KeyboardButton(text='общага')]],
    resize_keyboard=True, input_field_placeholder='Выберите пункт меню.')

catalogHistory = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='тема истории', callback_data='h1 theme'),
    InlineKeyboardButton(text='другая тема', callback_data='h2 theme')],
    [InlineKeyboardButton(text='третья тема', callback_data='h3 theme'),
    InlineKeyboardButton(text='четвёртая тема', callback_data= 'h4 theme')]])

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='тема обществознания', callback_data='об1 theme'),
    InlineKeyboardButton(text='другая тема', callback_data='об2 theme')],
    [InlineKeyboardButton(text='третья тема', callback_data='об3 theme'),
    InlineKeyboardButton(text='четвёртая тема', callback_data= 'об4 theme')]])