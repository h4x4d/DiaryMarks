from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_inline_keyboard = InlineKeyboardMarkup()

main_inline_keyboard.row(
    InlineKeyboardButton("✔️ Список предметов", callback_data="list_of_subjects")
)
main_inline_keyboard.row(
    InlineKeyboardButton("➕ Добавить новый предмет", callback_data="add_subject")
)
main_inline_keyboard.row(
    InlineKeyboardButton("⚙ Настройки", callback_data="settings")
)
