from aiogram import Router, types
from aiogram.filters.command import Command


picture_router = Router()


@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    file = types.FSInputFile("images/image.jfif")
    # await message.answer_photo(file, caption="")
    await message.answer_photo(photo=file, caption=f"beautiful image")
# можно использовать вместо answer использовать reply