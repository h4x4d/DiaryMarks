from aiogram import types
from keyboards.inline.subject_inline_keyboard import subject_keyboard

from data import Subject, create_session
from actions import actions

from bot_create import bot


async def bot_new_subject(msg: types.Message, user_id=None):
    back_keyboard = types.InlineKeyboardMarkup()
    back_keyboard.row(types.InlineKeyboardButton("⬅️️ Назад", callback_data="MAIN"))

    if not user_id:
        await msg.answer(f'Введите название нового предмета:',
                         reply_markup=back_keyboard)

        actions[msg.from_user.id] = "new_subject"
    else:
        await msg.edit_text(f'Введите название нового предмета:',
                            reply_markup=back_keyboard)

        actions[user_id] = "new_subject"


async def bot_new_subject_inline(call: types.CallbackQuery):
    await bot_new_subject(call.message, call.from_user.id)


async def bot_new_subject_second(msg: types.Message):
    del actions[msg.from_user.id]

    subject = Subject()
    subject.name = msg.text
    subject.user_id = msg.from_user.id

    session = create_session()
    session.add(subject)
    session.commit()

    keyboard = subject_keyboard(subject.id)

    await bot.delete_message(msg.from_user.id, msg.message_id - 1)
    await msg.delete()

    await msg.answer(f'Предмет: <i>{subject.name}</i>\n\n'
                     f'Оценки:\n'
                     f'<b>Нет</b>\n\n'
                     f'Средняя: <b>0.0</b>',
                     reply_markup=keyboard)
