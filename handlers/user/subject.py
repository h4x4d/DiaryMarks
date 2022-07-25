from aiogram import types

from data import Subject, create_session
from keyboards.inline.subject_inline_keyboard import subject_keyboard

from .list_of_subjects import bot_list_of_subjects


async def send_subject_message(call, subject):
    marks = list(subject.saved_marks + subject.unsaved_marks)

    if marks:
        i_marks = [int(i) for i in marks]
        sr = round(sum(i_marks) / len(i_marks), 2)
    else:
        sr = 0.0

    formatted_marks = "<b>" + "".join([mark if (ind + 1) % 4 != 0 else mark + " "
                                       for ind, mark in enumerate(subject.saved_marks)]) + "</b> " + \
                      "".join([mark if (ind + 1) % 4 != 0 else mark + " "
                               for ind, mark in enumerate(subject.unsaved_marks)])

    keyboard = subject_keyboard(subject.id)

    await call.message.edit_text(f'Предмет: <i>{subject.name}</i>\n\n'
                                 f'Оценки:\n'
                                 f'{"Нет" if not marks else formatted_marks}\n\n'
                                 f'Средняя: <b>{sr}</b>',
                                 reply_markup=keyboard)


async def bot_subject(call: types.CallbackQuery):
    await call.answer()
    session = create_session()

    subject: Subject = session.query(Subject).get(int(call.data.split('_')[2]))

    await send_subject_message(call, subject)


async def bot_edit_subject(call: types.CallbackQuery):
    await call.answer()
    session = create_session()

    subject: Subject = session.query(Subject).get(int(call.data.split('_')[2]))

    subject.unsaved_marks += call.data.split("_")[3]
    session.commit()

    await send_subject_message(call, subject)


async def bot_delete_subject(call: types.CallbackQuery):
    session = create_session()
    subject: Subject = session.query(Subject).get(int(call.data.split('_')[2]))

    if call.data.split('_')[3] == "one":
        await call.answer("")
        if subject.unsaved_marks == "":
            subject.saved_marks = subject.saved_marks[:-1]
        else:
            subject.unsaved_marks = subject.unsaved_marks[:-1]
    else:
        if subject.unsaved_marks == "":
            if subject.saved_marks == "":
                await call.answer("Предмет удален.")
                session.delete(subject)
                session.commit()

                await bot_list_of_subjects(call.message, user_id=call.from_user.id)

                return
            else:
                await call.answer("Нажмите еще раз чтобы удалить предмет.")
                subject.saved_marks = ""
        else:
            if subject.saved_marks:
                await call.answer("Нажмите еще раз чтобы удалить и сохраненные.")
            else:
                await call.answer("Нажмите еще раз чтобы удалить предмет.")

            subject.unsaved_marks = ""

    session.commit()

    await send_subject_message(call, subject)


async def bot_save_subject(call: types.CallbackQuery):
    session = create_session()
    await call.answer("Оценки сохранены.")

    subject: Subject = session.query(Subject).get(int(call.data.split('_')[2]))
    subject.saved_marks = subject.saved_marks + subject.unsaved_marks
    subject.unsaved_marks = ""

    session.commit()

    await send_subject_message(call, subject)


