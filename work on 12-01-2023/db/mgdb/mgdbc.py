import psycopg2 as pgc


class Config(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            # cls._instance.__password = 'aloha'
            #
            # cls._instance._client = pymongo.MongoClient(
            #     f"mongodb+srv://aloha:{cls._instance.__password}@aloha.cvmftvt.mongodb.net/?retryWrites=true&w=majority")

        return cls._instance


class Connection(Config):
    def __init__(self, db):
        self.__db = db
        self.__user = 'postgres'
        self.__host = 'localhost'
        self.__password = 'harshit'
        try:
            self.__conn = pgc.connect(
                host=self.__host,
                database=self.__db,
                user=self.__user,
                password=self.__password,
                port="5432"
            )
            self._cur = self.__conn.cursor()
        except Exception as error:
            self.__notify(error)

    @staticmethod
    def __notify(error):
        """
        give error message while exception are happened

        ARGS:
            error (str) : Error that are happened while connecting database

        RETURN:
            str : Error message

        """
        return error



if __name__ == '__main__':
    c1 = Connection('thunder')
    print(c1)
    c2 = Connection('erp')
    print(c2)
