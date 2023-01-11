import mysql.connector as myc


class _Connection:

    def __init__(self, db):
        self.__db = db
        self.__user = 'root'
        self.__host = 'localhost'
        self.__password = ''
        try:
            self.__conn = myc.connect(
                host=self.__host,
                database=self.__db,
                user=self.__user,
                password=self.__password,
                port="3306"
            )
            self._cur = self.__conn.cursor()
        except Exception as error:
            self.__notify(error)

    def save(self):
        """
        save the data in the tables
        """
        self.__conn.commit()

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

    def __repr__(self):
        """
        Return the object of _Connection class

        RETURN:
            str: which database connected
        """
        return f'{self.__db} database has connected.'

    def __del__(self):
        self._cur.close()
        self.__conn.close()
