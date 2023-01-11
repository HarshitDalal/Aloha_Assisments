from .postgresqlc import _Connection


class Employee(_Connection):
    """
    Class that handel all operation that are perform on employee table

    ARGS::
        _Connection (class): inherit form pgdb.postgres
    """

    def __init__(self):
        """
        Call the base class constructor with database name as a parameter
        """
        super().__init__('thunder')

    def add(self, name, email, phone, company):
        """
        Add or Insert new detail about Employee in a employee table.

        ARGS:
            name (str): name of employee
            email (str): email of employee
            phone (str): phone number of employee
            company (int): primary key of company table where employee work
        """

        sql = 'INSERT INTO employee (name, email, phone, company) VALUES (%s, %s, %s, %s)'
        values = (name, email, phone, company)
        self._cur.execute(sql, values)

    def modify(self, eid, name, email, phone, company):
        """
        Modify or Update detail about Employee in a employee table.

        ARGS:
            eid (int): which one employee detail you have to change
            name (str): name of employee
            email (str): email of employee
            phone (str): phone number of employee
            company (int): primary key of company table where employee work
        """
        try:
            sql = 'UPDATE employee SET name = %s, email = %s, phone = %s, company = %s WHERE eid = %s'
            values = (name, email, phone, company, eid)
            self._cur.execute(sql, values)
        except Exception as e:
            return e

    def remove(self, eid):
        """
        Remove or Delete detail about Employee in a employee table.

        ARGS:
            eid (int): primary key of employee table
        """
        try:
            sql = 'DELETE FROM employee WHERE eid = %s'
            self._cur.execute(sql, (eid,))
        except Exception as e:
            return e

    def all_data(self):
        """
        Provide all the rows of the employee table

        RETURN:
            list: list of tuples. tuples holds detail about employee
        """

        sql = 'SELECT * FROM employee'
        self._cur.execute(sql)
        return self._cur.fetchall()

    def data_by_id(self, eid):
        """
        Provide single employee detail who have same eid that user give

        ARGS::
            eid (int): primary key of employee table

        RETURN:
            tuple: single tuple that holds only single employee detail
        """
        try:
            sql = 'SELECT * FROM employee WHERE eid = %s'
            self._cur.execute(sql, (eid,))
            return self._cur.fetchone()
        except Exception as e:
            return e

    def size_data(self, size):
        """
        Number of rows are fetch from employee table

        ARGS:
            size (int): number of rows

        RETURN:
            list: return a list of tuples that are less or equal to size
        """
        sql = 'SELECT * FROM employee'
        self._cur.execute(sql)
        return self._cur.fetchmany(size)
