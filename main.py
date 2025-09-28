from aiogram import Bot, Dispatcher
import asyncio

from app.handlers import router
from app.Utils import token

async def main():
    bot = Bot(token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


#запустить main 
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("бот выключен")



