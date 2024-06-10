import asyncio
import logging

from config import dp, bot
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.picture import picture_router


async def main():
    # регистрируем роутер
    dp.include_router(start_router)
    dp.include_router(echo_router)
    dp.include_router(picture_router)
    # запускаем бот
    await dp.start_polling(bot)


if __name__=="__main__":
    # logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)')
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

