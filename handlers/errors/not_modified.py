from aiogram import types
from aiogram.utils import exceptions


async def message_not_modified(_: types.Update, __: exceptions.MessageNotModified):
    return True


async def message_to_delete_not_found(_: types.Update, __: exceptions.MessageToDeleteNotFound):
    return True
