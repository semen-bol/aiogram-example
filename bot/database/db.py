import asyncio

# В данной реализации доступен только метод findOne, ознакомьтесь с данной базой
# данных и реализуйте сами остальные методы такие как insert_one, delete_one, delete_many
# и т.д, по примеру findOne (метод тут в самом низу)
# Файл test.py из этой директории можно удалить, но перед этим рекомендую его посмотреть

from motor.motor_asyncio import AsyncIOMotorClient

class db:
    def __init__(self, host: str, username: str, password: str, database: str, isLocal = False) -> None:
        self._host = host
        self._username = username
        self._password = password
        self._database = database

        self.client = None
        self.db = None
        self._connect(isLocal)

    def _connect(self, isLocal):
        if isLocal == False:
            connect_url_auto = "mongodb://{username}:{password}@{host}/?authSource={database}".format(
                username=self._username,
                password=self._password,
                host=self._host,
                database=self._database
            )
        elif isLocal == True:
            connect_url_auto = "mongodb://{host}/?authSource={database}".format(host=self._host,database=self._database)
        
        self.client = AsyncIOMotorClient(connect_url_auto)
        self.db = self.client[self._database]
    
    async def ping(self):
        if await self.client.admin.command("ping"):
            return True
        else: return False

    async def findOne(self, collection: str, document: dict):
        collection_ = self.db[collection]
        result = await collection_.find_one(document)
        return result

    
