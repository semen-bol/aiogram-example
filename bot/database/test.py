import asyncio

from mongo_db import init_db as db
#from sqlite_db import db as sqlite_db

from loguru import logger

# SQLite
"""async def example_sqlite():
    sql = sqlite_db("./example.db")
    await sql.connect()
    passt = await sql.ping()
    if passt == True: logger.debug("Подключение с бд успешно установлно")
    else: logger.debug("Неудачное подключение к бд!");
    s = await sql.prompt("SELECT * FROM users")
    print(s)
    try:
        await sql._exit()
    except ValueError as err: logger.debug("Ошибка... Отключение от базы данных.")
    print(s)"""

# Mongo
async def example():
    logger.info("Подключаю базу данных...")
    ping = await db.ping()

    if ping == True:
        logger.debug("База данных подключена")
    else: logger.debug("База данных не смогла ответить на запрос")

if __name__ == "__main__":
    try:
        asyncio.run(example())
    except KeyboardInterrupt:
        logger.debug("Exiting...")
