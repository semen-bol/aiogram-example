import asyncio

from db import db
from mysql_db import db as mysql_db
from loguru import logger

# SQLite
async def example_sqlite():
    sql = mysql_db("example.db")
    await sql.connect()
    passt = await sql.ping()
    if passt == True: logger.debug("Подключение с бд успешно установлно")
    else: logger.debug("Неудачное подключение к бд! Завершаю процесс..."); return
    s = await sql.prompt("SELECT * FROM users")
    print(s)
    try:
        await sql._exit()
    except ValueError as err: logger.debug("Отключение от базы данных.")
    print(s)

# Mongo
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
    asyncio.run(example_sqlite())
