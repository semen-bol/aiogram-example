# С костылями но своё ;D
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message
from cachetools import TTLCache
from bot.utils.func import checkForCommand, cmdnoprefandargs
from loguru import logger


class CommandFlood(BaseMiddleware):
    def __init__(self, time_limit: int=4) -> None:
        self.limit = TTLCache(10_000, ttl=time_limit) # создаем кэш ))))

    async def __call__(
            self, 
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
            event: Message, 
            data: Dict[str, Any],
        ) -> Any:
            if not event.message_id or not event.text: return await handler(event, data) # проверка на отсеивание других евентов по типу инвайта в чат других юзеров
            else: pass
            if event.chat.id in self.limit and event.from_user.id in self.limit: # есть ли пользователь в кэше
                if self.limit[event.chat.id]['answer'] == 1 and self.limit[event.chat.id]['user'] == event.from_user.id and self.limit[event.chat.id]['cmd'] == cmdnoprefandargs(list(event.text)):
                    # ахуеть какие длинные условия, но так надо, да - продолжаем
                    if checkForCommand(list(event.text)) == False: return #не команда? - отменяем все и просто return
                    await event.reply(text=f"Нельзя так часто использовать команду эту команду. Повторите попытку через несколько секунд!"); self.limit[event.chat.id]['answer'] = 2
                    # ОБОЖЕ, это команда, отправляем сообщение о том что низя так, и делаем так что бы переменная answer была равна 1, что бы не отвечать на каждый спам,
                    # тем самым не перегружая бота
                    logger.info(f"{event.from_user.id} {event.from_user.first_name} получил пред. сообщение"); return # не возвращаем команду и логируем
                elif self.limit[event.chat.id]['answer'] == 2 and self.limit[event.chat.id]['user'] == event.from_user.id and self.limit[event.chat.id]['cmd'] == cmdnoprefandargs(list(event.text)):
                    # уже получал ответ на свой спам? иди нахуй! Возвращаем ничего
                    return
                else: pass
            else: # нету:
                if checkForCommand(list(event.text)) == True: # текст который ввел пользователь - команда? СМОТРИТЕ МЕТОД checkForCommand
                    # da
                    self.limit[event.chat.id] = { "user": event.from_user.id, "cmd": cmdnoprefandargs(list(event.text)) , "answer": 1 } # добавлеяем в кэш
                    logger.info(f"{event.from_user.id} {event.from_user.first_name} выполнил команду [{cmdnoprefandargs(list(event.text))}] и получил кд 4 секунды") # логирем
                else: # net
                    pass # дальше иди
            return await handler(event, data) # пропускаем текст или команду...