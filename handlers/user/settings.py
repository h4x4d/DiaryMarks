from aiogram import types

from actions import actions
from keyboards.inline.settings_inline_keyboard import settings_keyboard

from data import create_session, User, Subject

from mos_ru.get_token_from_curl import get_data_from_curl
from mos_ru.get_marks import get_marks
from mos_ru.marks_process import get_all_marks

from bot_create import bot


async def bot_settings(msg: types.Message, user_id=None):
    if not user_id:
        await msg.answer(f'Настройки бота:',
                         reply_markup=settings_keyboard)

    else:
        await msg.edit_text(f'Настройки бота:',
                            reply_markup=settings_keyboard)


async def bot_settings_inline(call: types.CallbackQuery):
    await call.answer()
    await bot_settings(call.message, call.from_user.id)


async def bot_settings_delete(call: types.CallbackQuery):
    await call.answer("Все предметы удалены")

    session = create_session()
    user: User = session.query(User).get(call.from_user.id)

    for i in user.subjects:
        session.delete(i)

    session.commit()


async def bot_settings_token(call: types.CallbackQuery):
    await call.answer()

    back_keyboard = types.InlineKeyboardMarkup()
    back_keyboard.row(types.InlineKeyboardButton("Гайд по получению token", "example.com"))
    back_keyboard.row(types.InlineKeyboardButton("⬅️️ Назад", callback_data="MAIN"))

    await call.message.answer("Данный функционал позволяет получить все оценки из вашего mos.ru и занести их в базу."
                              "\n\n<b>⚠ Мы не храним ваши token ключи на сервере, "
                              "они используются только во время операции а далее удаляются</b>\n\n"
                              "Введите ваш токен с mos.ru:",
                              reply_markup=back_keyboard)

    actions[call.from_user.id] = "mos_ru_token"


async def bot_mos_ru_token(msg: types.Message):
    token, student_id = get_data_from_curl(msg.text)
    print(token, student_id)

    data = get_marks(token, student_id)
    print(data)
    marks = get_all_marks(data)

    session = create_session()

    for sub in marks:
        subject = Subject()
        subject.name = sub
        subject.user_id = msg.from_user.id
        subject.saved_marks = "".join([str(i) for i in marks[sub]])

        session.add(subject)

    session.commit()

    await bot.delete_message(msg.from_user.id, msg.message_id - 1)
    await msg.delete()

    await msg.answer("Парсинг завершен. Проверьте список предметов.")


