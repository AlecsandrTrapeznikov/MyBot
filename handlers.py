from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
import asyncio
from aiogram.filters import CommandStart, Command

import app.keyboards as kb
from app.Utils import token

router = Router()

Bot = Bot(token)

message_ids = list()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!', reply_markup=kb.main) 

@router.message(F.text == 'история')
async def cmd_history(message: Message):
    await message.answer_photo(photo= 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg/330px-The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg', 
                               caption='выбрать тему по истории:!', reply_markup=kb.catalogHistory)


@router.message(F.text == 'общага')
async def cmd_history(message: Message):
    await message.answer_photo(photo= 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg/330px-The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg', 
                               caption='выбрать тему по обществознанию:', reply_markup=kb.catalog)

@router.callback_query(F.data == 'h1 theme')
async def cmd_h1theme(callback: CallbackQuery):
    a = await callback.message.answer('введити команду: /testh, для начала теста по истории')
    message_ids.append(a.message_id)

@router.callback_query(F.data == 'h2 theme')
async def cmd_h1theme(callback: CallbackQuery):
    a = await callback.message.answer('текст для 2ой темы истории')
    message_ids.append(a.message_id)

@router.callback_query(F.data == 'h3 theme')
async def cmd_h1theme(callback: CallbackQuery):
    a = await callback.message.answer('текст для 3ей темы истории')
    message_ids.append(a.message_id)  

@router.callback_query(F.data == 'h4 theme')
async def cmd_h1theme(callback: CallbackQuery):
    a = await callback.message.answer('тест по темам истории')
    message_ids.append(a.message_id)

@router.message(Command("testh"))
async def test(message: Message):
    message.answer('тест начат:')
    for id in message_ids:
        await Bot.delete_message(chat_id = message.chat.id,message_id = id)

@router.callback_query(F.data == 'об1 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.message.answer('текст для 1ой темы обществознания')

@router.callback_query(F.data == 'об2 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.message.answer('текст для 2ой темы обществознания')

@router.callback_query(F.data == 'об3 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.message.answer('текст для 3ой темы обществознания')   

@router.callback_query(F.data == 'об4 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.message.answer('текст для 4ой темы обществознания')

