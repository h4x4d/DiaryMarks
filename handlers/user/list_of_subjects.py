from aiogram import types

from data import User, create_session, Subject

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def bot_list_of_subjects(msg: types.Message, user_id=None):
    session = create_session()

    user = session.query(User).get(msg.from_id if not user_id else user_id)

    keyboard = InlineKeyboardMarkup()
    last = None

    for elem in user.subjects:
        if last:
            keyboard.row(last, InlineKeyboardButton(elem.name, callback_data=f"open_subject_{elem.id}"))
            last = None
        else:
            last = InlineKeyboardButton(elem.name, callback_data=f"open_subject_{elem.id}")

    if last:
        keyboard.row(last)

    keyboard.row(types.InlineKeyboardButton("⬅️️ Назад", callback_data="MAIN"))

    if not user_id:
        await msg.answer(f'Список добавленных вами предметов:',
                         reply_markup=keyboard)
    else:
        await msg.edit_text(f'Список добавленных вами предметов:',
                            reply_markup=keyboard)


async def bot_list_of_subjects_inline(call: types.CallbackQuery):

    if call.data.split("_")[-1].isdigit():
        await call.answer("Все несохраненные оценки были удалены")
        session = create_session()
        subject: Subject = session.query(Subject).get(int(call.data.split("_")[-1]))
        subject.unsaved_marks = ""
        session.commit()
    else:
        await call.answer()

    await bot_list_of_subjects(call.message, user_id=call.from_user.id)
