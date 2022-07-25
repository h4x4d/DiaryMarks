from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

settings_keyboard = InlineKeyboardMarkup()
settings_keyboard.row(
    InlineKeyboardButton("❌ Удалить все предметы", callback_data="delete_all_subjects")
)
settings_keyboard.row(
    InlineKeyboardButton("⚠ Скопировать оценки из журнала", callback_data="parse_marks_from_token")
)
settings_keyboard.row(InlineKeyboardButton("⬅️️ Назад", callback_data="MAIN"))
