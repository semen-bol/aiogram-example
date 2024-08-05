######################################################################################################
# Более подробно о updates можете прочитать в документации, и реализуйте это по примеру!
# В моем случае (чат - менеджер) это нужно для ивентов таких как chat_member и my_chat_member
######################################################################################################

from aiogram import F, Router
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, MEMBER, KICKED
from aiogram.types import ChatMemberUpdated, Message

rt = Router()

@rt.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=KICKED)
)
async def user_blocked_bot(event: ChatMemberUpdated):
    print(event)


@rt.my_chat_member(
    ChatMemberUpdatedFilter(member_status_changed=MEMBER)
)
async def user_unblocked_bot(event: ChatMemberUpdated):
    print(event)