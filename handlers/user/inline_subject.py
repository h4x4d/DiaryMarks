import hashlib
import random

from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from data import create_session, User, Subject


async def inline_subject(inline_query: InlineQuery):
    answer = []
    text = inline_query.query.lower()

    session = create_session()
    user: User = session.query(User).get(inline_query.from_user.id)

    if not user:
        ans = InlineQueryResultArticle(
            id=str(random.getrandbits(64)),
            title='Кажется, вы не зарегистрированы',
            input_message_content=InputTextMessageContent(f'Бот: @DiaryMarks_robot', parse_mode="HTML"),
            description=f'Бот: @DiaryMarks_robot'
        )
        await inline_query.answer([ans], cache_time=1)
        return

    subjects: list[Subject] = user.subjects

    for subject in subjects:
        if text in subject.name.lower():
            result_id: str = hashlib.md5(str(subject.id).encode()).hexdigest()

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

            ans = InlineQueryResultArticle(
                id=result_id,
                title=subject.name,
                input_message_content=InputTextMessageContent(f'Предмет: <i>{subject.name}</i>\n\n'
                                                              f'Оценки:\n'
                                                              f'{"Нет" if not marks else formatted_marks}\n\n'
                                                              f'Средняя: <b>{sr}</b>', parse_mode="HTML"),
                description=f'Средняя: {sr}'
            )
            answer.append(ans)

    if not answer:
        ans = InlineQueryResultArticle(
            id=str(random.getrandbits(64)),
            title='Ничего не найдено',
            input_message_content=InputTextMessageContent(f'Бот: @DiaryMarks_robot', parse_mode="HTML"),
            description=f'Нажав сюда вы сгенерируете мини-рекламу:)'
        )
        answer.append(ans)

    await inline_query.answer(answer, cache_time=1)
