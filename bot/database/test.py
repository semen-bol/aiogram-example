import asyncio

from db import db
from loguru import logger

db = db(host="localhost:27017",
        username=None, 
        password=None, 
        database="example", 
        isLocal=True)

async def example():
    logger.info("Подключаю базу данных...")
    ping = await db.ping()

    if ping == True:
        logger.debug("База данных подключена")
    else: logger.debug("База данных не смогла ответить на запрос")

if __name__ == "__main__":
    asyncio.run(example())
