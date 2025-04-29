#soon

"""import aiosqlite

class db:
    def __init__(self, path):
        self._path_to_db = path

    async def connect(self):
        self.conn = await aiosqlite.connect(self._path_to_db)
        self.curs = await self.conn.cursor()

    async def ping(self):
        try:
            self.conn.execute()
        except Exception as ex: return False

    async def prompt(self, prompt):
        try:
            s = await self.conn.execute(prompt)
            await s.close()
        except Exception as err:
            if err == None: print(f"unknown err with {prompt}")
            print(err);

    async def _exit(self):
        await self.conn.close()
        await self.curs.close()"""