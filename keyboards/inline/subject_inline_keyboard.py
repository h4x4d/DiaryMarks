from aiogram import types


def subject_keyboard(subject_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton("5", callback_data=f"subject_mark_{subject_id}_5"),
        types.InlineKeyboardButton("4", callback_data=f"subject_mark_{subject_id}_4")
    )
    keyboard.row(
        types.InlineKeyboardButton("3", callback_data=f"subject_mark_{subject_id}_3"),
        types.InlineKeyboardButton("2", callback_data=f"subject_mark_{subject_id}_2")
    )

    keyboard.row(
        types.InlineKeyboardButton("❌ Удалить последнюю", callback_data=f"subject_delete_{subject_id}_one")
    )
    keyboard.row(
        types.InlineKeyboardButton("📛 Удалить все", callback_data=f"subject_delete_{subject_id}_all")
    )
    keyboard.row(
        types.InlineKeyboardButton("✅ Сохранить", callback_data=f"subject_save_{subject_id}_all")
    )

    keyboard.row(types.InlineKeyboardButton("⬅️️ Назад", callback_data=f"list_of_subjects_{subject_id}"))

    return keyboard
