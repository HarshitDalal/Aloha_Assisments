from .postgresqlc import _Connection


class Company(_Connection):
    """
    Class that handel all operation that are perform on company table

    ARGS:
        _Connection (class): inherit form pgdb.postgres
    """

    def __init__(self):
        """
        Call the base class constructor with database name as a parameter
        """
        super().__init__('thunder')

    def add(self, name, ctype, location):
        """
        Add or Insert new detail about Company in a company table.

        ARGS:
            name (str): name of company
            ctype (str): type of company
            location (str): location of company
        """

        sql = 'INSERT INTO company (name, type, location) VALUES (%s, %s, %s)'
        values = (name, ctype, location)
        self._cur.execute(sql, values)
        self._save()

    def modify(self, cid, name, ctype, location):
        """
        Modify or Update detail about Company in a company table.

        ARGS:
            cid (int): which one company detail you have to change
            name (str): name of company
            ctype (str): type of company
            location (str): location of company
        """
        try:
            sql = 'UPDATE company SET name = %s, type = %s, location = %s WHERE cid = %s'
            values = (name, ctype, location, cid)
            self._cur.execute(sql, values)
            self._save()
        except Exception as e:
            return e

    def remove(self, cid):
        """
        Remove or Delete detail about Company in a company table.

        ARGS:
            cid (int): primary key of company table
        """
        try:
            sql = 'DELETE FROM company WHERE cid = %s'
            self._cur.execute(sql, (cid,))
            self._save()
        except Exception as e:
            return e

    def all_data(self):
        """
        Provide all the rows of the company table

        RETURN:
            list: list of tuples. tuples holds detail about company
        """

        sql = 'SELECT * FROM company'
        self._cur.execute(sql)
        return self._cur.fetchall()

    def data_by_id(self, cid):
        """
        Provide single company detail who have same cid that user give

        ARGS:
            cid (int): primary key of company table

        RETURN:
            tuple: single tuple that holds only single company detail
        """
        try:
            sql = 'SELECT * FROM company WHERE eid = %s'
            self._cur.execute(sql, (cid,))
            return self._cur.fetchone()
        except Exception as e:
            return e

    def size_data(self, size):
        """
        Number of rows are fetch from company table

        ARGS:
            size (int): number of rows

        RETURN:
            list: return a list of tuples that are less or equal to size
        """
        sql = 'SELECT * FROM company'
        self._cur.execute(sql)
        return self._cur.fetchmany(size)
