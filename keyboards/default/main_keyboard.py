from aiogram.types import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

main_keyboard.row(
    "✔️ Список предметов"
)
main_keyboard.row(
    "➕ Добавить новый предмет"
)
main_keyboard.row(
    "⚙ Настройки"
)
