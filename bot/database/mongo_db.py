# Подготовил более красивую и готовую версию базы данных
# могут быть ошибки в ходе работы...

from motor.motor_asyncio import AsyncIOMotorClient

class MongoDB:
    def __init__(
        self,
        database: str,
        host: str = None,
        username: str = None,
        password: str = None,
        myUrl: str = None,
        isLocal=False,
    ) -> None:
        self._myUrl = myUrl

        self._host = host
        self._username = username
        self._password = password
        self._database = database

        self.client = None
        self.db = None

        self._connect(isLocal)

    def _connect(self, isLocal):
        if isLocal == False and not self._myUrl:
            connect_url_auto = (
                "mongodb://{username}:{password}@{host}/{database}?authSource=admin".format(
                    username=self._username,
                    password=self._password,
                    host=self._host,
                    database=self._database,
                )
            )
        elif isLocal == True and not self._myUrl:
            connect_url_auto = "mongodb://{host}/{database}?authSource=admin".format(
                host=self._host, database=self._database
            )
        elif self._myUrl:
            connect_url_auto = self._myUrl

        self.client = AsyncIOMotorClient(connect_url_auto)
        self.db = self.client[self._database]

    async def ping(self):
        if await self.client.admin.command("ping"):
            return True
        else:
            return False

    async def insertOne(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.insert_one(dict)

            return result
        except Exception as e:
            return e

    async def insertMany(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.insert_many(document)

            return result
        except Exception as e:
            return e

    async def find(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.find(document)

            return result
        except Exception as e:
            return e

    async def findOne(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.find_one(document)

            return result
        except Exception as e:
            return e

    async def deleteOne(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.delete_one(document)

            return result
        except Exception as e:
            return e

    async def deleteMany(self, collection: str, document: dict):
        try:
            collection_ = self.db[collection]
            result = await collection_.delete_many(document)

            return result
        except Exception as e:
            return e


init_db = MongoDB(host="mongo:27017", # host:port
        username="root", # root
        password="password", # qwerty123
        database="local", # users / example / chats
        isLocal=False # база данных локальна? boolean
        )