from aiogram import types


async def bot_stub(call: types.CallbackQuery):
    await call.answer("Этот функционал временно отключен.")