from aiogram import Router, types


echo_router = Router()


@echo_router.message()
async def echo_handler(message: types.Message):
    # await message.answer(message.text)
    await message.reply("Я вас не понимаю, вот команды которые я понимаю: "
                        "\n/start"
                        "\n/picture")