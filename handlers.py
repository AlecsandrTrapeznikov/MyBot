from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
import asyncio
from aiogram.filters import CommandStart, Command
#from aiogram.fsm.state import State, StatesGroup
#from aiogram.fsm import FSMContext

import app.keyboards as kb

router = Router()

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('хэлп')

#ловит сообшения /start, и запускает cmd_start.
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
    await callback.answer('')
    await callback.message.answer('текст для 1ой темы истории')

@router.callback_query(F.data == 'h2 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('текст для 2ой темы истории')

@router.callback_query(F.data == 'h3 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('текст для 3ей темы истории')

@router.callback_query(F.data == 'h4 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('тест по темам истории')


@router.callback_query(F.data == 'об1 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('текст для 1ой темы обществознания')

@router.callback_query(F.data == 'об2 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('текст для 2ой темы обществознания')

@router.callback_query(F.data == 'об3 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('текст для 3ой темы обществознания')   

@router.callback_query(F.data == 'об4 theme')
async def cmd_h1theme(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer('текст для 4ой темы обществознания')

