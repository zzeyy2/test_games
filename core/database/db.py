import aiosqlite
from sqlite3 import IntegrityError, OperationalError


class GameDB():

    def __init__(self, db_file):
        self.db_name = db_file

    async def initialize(self):
        self.connection = await aiosqlite.connect(self.db_name)

    async def search(self, title: str = None, publisher: str = None, year: int = None):
        cursor = await self.connection.cursor()
        query = 'SELECT * FROM games WHERE '
        conditions = []
        values = []

        if title:
            conditions.append("title = ?")
            values.append(title)
        if publisher:
            conditions.append("publisher = ?")
            values.append(publisher)
        if year:
            conditions.append("year = ?")
            values.append(year)

        query += " AND ".join(conditions)

        try:
            cursor = await self.connection.execute(query, tuple(values))
            return await cursor.fetchall()
        
        except OperationalError:
            return False

    async def add(self, title: str, publisher: str, year: int):
        try:

            if not await self.search(title):

                cursor = await self.connection.cursor()
                await cursor.execute("INSERT INTO games(title, publisher, year) VALUES (?, ?, ?)", (title, publisher, year,))
                await self.connection.commit()
                
                return True
            
            else:
                
                return False
            
        except IntegrityError:
            return False

    async def remove(self, title: str = None, publisher: str = None, year: int = None):
        cursor = await self.connection.cursor()

        if await self.search(title):
            query = 'DELETE FROM games WHERE '
            conditions = []
            values = []

            if title:
                conditions.append("title = ?")
                values.append(title)
            if publisher:
                conditions.append("publisher = ?")
                values.append(publisher)
            if year:
                conditions.append("year = ?")
                values.append(year)

            query += " AND ".join(conditions)
            cursor = await self.connection.execute(query, tuple(values))

            await self.connection.commit()

            
            return True
        
        else:
            
            return False

    async def get_all(self):
        cursor = await self.connection.cursor()
        await cursor.execute("SELECT * FROM games")
        return await cursor.fetchall()

    async def edit(self, title: str = None, publisher: str = None, year: int = None,
                   new_title: str = None, new_publisher: str = None, new_year: int = None):
        
        if await self.search(title, publisher, year):

            query = 'UPDATE games SET '
            conditions = []
            new_Data = []

            if new_title:
                new_Data.append(f'title = "{new_title}"')
            if new_publisher:
                new_Data.append(f'publisher = "{new_publisher}"')
            if new_year:
                new_Data.append(f'year = "{new_year}"')


            if title:
                conditions.append(f'title = "{title}"')
            if publisher:
                conditions.append(f'publisher = "{publisher}"')
            if year:
                conditions.append(f'year = "{year}"')

            query += ", ".join(new_Data)
            query += " WHERE "
            query += " AND ".join(conditions)
            cursor = await self.connection.execute(query)

            await self.connection.commit()
            
            return True
        
        else:
            
            return False
