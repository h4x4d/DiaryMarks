from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, CommandHelp, Text

from .help import bot_help
from .start import bot_start, bot_start_inline
from .new_subject import bot_new_subject, bot_new_subject_second, bot_new_subject_inline
from .list_of_subjects import bot_list_of_subjects, bot_list_of_subjects_inline
from .subject import bot_subject, bot_edit_subject, bot_delete_subject, bot_save_subject
from .settings import bot_settings, bot_settings_inline, bot_settings_delete, bot_settings_token, bot_mos_ru_token
from .bot_stub import bot_stub
from .inline_subject import inline_subject

from filters import ActionFilter


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
    dp.register_message_handler(bot_help, CommandHelp())

    dp.register_message_handler(bot_new_subject, Text("➕ Добавить новый предмет"))
    dp.register_message_handler(bot_list_of_subjects, Text("✔️ Список предметов"))
    dp.register_message_handler(bot_settings, Text("⚙ Настройки"))

    dp.register_message_handler(bot_new_subject_second, ActionFilter("new_subject"))
    dp.register_message_handler(bot_mos_ru_token, ActionFilter("mos_ru_token"))

    dp.register_callback_query_handler(bot_subject, Text(startswith="open_subject"))
    dp.register_callback_query_handler(bot_new_subject_inline, Text(startswith="add_subject"))
    dp.register_callback_query_handler(bot_edit_subject, Text(startswith="subject_mark"))
    dp.register_callback_query_handler(bot_settings_inline, Text(startswith="settings"))
    dp.register_callback_query_handler(bot_settings_delete, Text(startswith="delete_all_subjects"))
    dp.register_callback_query_handler(bot_settings_token, Text(startswith="parse_marks_from_token"))
    dp.register_callback_query_handler(bot_delete_subject, Text(startswith="subject_delete_"))
    dp.register_callback_query_handler(bot_stub, Text(startswith="parse_marks_from_token"))
    dp.register_callback_query_handler(bot_save_subject, Text(startswith="subject_save"))
    dp.register_callback_query_handler(bot_list_of_subjects_inline, Text(startswith="list_of_subjects"))
    dp.register_callback_query_handler(bot_start_inline, Text("MAIN"))

    dp.register_inline_handler(inline_subject)
