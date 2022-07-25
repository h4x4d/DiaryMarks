from aiogram import types

from data import User, create_session
from keyboards.default.main_keyboard import main_keyboard
from keyboards.inline.main_inline_keyboard import main_inline_keyboard

from actions import actions


async def bot_start(msg: types.Message):
    session = create_session()

    if not session.query(User).get(msg.from_id):
        user = User()
        user.id = msg.from_id
        user.username = msg.from_user.username

        session.add(user)
        session.commit()

    await msg.answer(f'Привет, {msg.from_user.full_name}! Этот бот поможет тебе подсчитывать возможные '
                     f'варианты событий со школьными оценками!',
                     reply_markup=main_keyboard)


async def bot_start_inline(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(f'Привет, {call.from_user.full_name}! '
                                 f'Этот бот поможет тебе подсчитывать возможные '
                                 f'варианты событий со школьными оценками!',
                                 reply_markup=main_inline_keyboard)
    if call.from_user.id in actions:
        del actions[call.from_user.id]
