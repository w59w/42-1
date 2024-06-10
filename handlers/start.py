from aiogram import Router, types, F
from aiogram.filters.command import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    # print("Message", message)
    # print("User info", message.from_user)
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://t.me/example")
            ],
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com/example")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="Пожертвуйте нам", callback_data="donate")
            ]
        ]
    )
    name = message.from_user.first_name
    await message.answer(f"Hello, {name}!", reply_markup=keyboard)  # Отправляем клавиатуру вместе с сообщением


@start_router.callback_query(F.data == "about")
async def about_handler(callback: types.CallbackQuery):
    await callback.answer()   # для того чтобы бот не зависал
    await callback.message.answer("Мы бот")


@start_router.callback_query(F.data == "donate")
async def about_handler(callback: types.CallbackQuery):
    await callback.answer()   # для того чтобы бот не зависал
    await callback.message.answer("Спасибо!")
