from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

settings_keyboard = InlineKeyboardMarkup()
settings_keyboard.row(
    InlineKeyboardButton("❌ Удалить все предметы", callback_data="delete_all_subjects")
)
settings_keyboard.row(
    InlineKeyboardButton("⚠ Скопировать оценки из журнала", callback_data="parse_marks_from_token")
)
settings_keyboard.row(
    InlineKeyboardButton("Репозиторий на GitHub", "https://github.com/h4x4d/DiaryMarks")
)
settings_keyboard.row(InlineKeyboardButton("⬅️️ Назад", callback_data="MAIN"))
