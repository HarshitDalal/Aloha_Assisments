import psycopg2


class Connection:
    ''' This class only for establish connection with PostgreSQL '''

    def __init__(self):
        self.__db = 'erp'
        self.__user = 'postgres'
        self.__host = 'localhost'
        self.__password = 'harshit'

        self._conn = psycopg2.connect(
            host=self.__host,
            database=self.__db,
            user=self.__user,
            password=self.__password,
            port="5432"
        )
        self._cur = self._conn.cursor()

    def save(self):
        self._conn.commit()

    def __del__(self):
        self._cur.close()
        self._conn.close()
