from aiogram import Bot, Dispatcher
import asyncio

from app.handlers import router

async def main():
    bot = Bot(token='8252650065:AAGKElwAX-jrcbBc4axru_72a34pQzgDAU4')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


#запустить main 
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("бот выключен")


