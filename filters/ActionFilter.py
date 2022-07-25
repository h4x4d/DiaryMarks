from typing import Union

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, InlineQuery, Poll

from actions import actions


class ActionFilter(BoundFilter):
    def __init__(self, action):
        self.action = action

    async def check(self, obj: Union[Message, CallbackQuery, InlineQuery, Poll]):
        user_id = obj.from_id

        if user_id in actions and actions[user_id].startswith(self.action):
            return True
        else:
            return False
