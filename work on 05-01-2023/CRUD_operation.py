import psycopg2


class Crud_Op:

    def __init__(self):
        self.__conn = psycopg2.connect(
            host="localhost",
            database="student",
            user="postgres",
            password="harshit",
            port="5432"
        )
        self.__cur = self.__conn.cursor()

    def insert_data(self, s_name, rolln, phone, email, course):
        SQL = "INSERT INTO stud (s_name, rolln, phone, email, course) VALUES (%s ,%s, %s, %s, %s)"

        values = (s_name, rolln, phone, email, course)
        print('Inserting data ...')
        self.__cur.execute(SQL, values)
        print('Data inserted')

        self.__conn.commit()

    def delete_data(self, *eno):
        SQL = "DELETE FROM stud WHERE eno IN(%s)"

        values = eno
        try :
            print('Deleting data ...')
            self.__cur.execute(SQL, values)
            print('Data Delete')

            self.__conn.commit()
        except Exception as e:
            print(e)

    def update_data(self, eno, **kwargs):
        if list(kwargs.keys()) == ['s_name']:
            SQL = "UPDATE stud SET s_name = %s WHERE eno = %s"
            values = (kwargs['s_name'], eno)
        elif list(kwargs.keys()) == ['email']:
            SQL = "UPDATE stud SET email = %s WHERE eno = %s"
            values = (kwargs['email'], eno)
        elif list(kwargs.keys()) == ['phone']:
            SQL = "UPDATE stud SET phone = %s WHERE eno = %s"
            values = (kwargs['phone'], eno)
        elif list(kwargs.keys()) == ['course']:
            SQL = "UPDATE stud SET email = %s WHERE eno = %s"
            values = (kwargs['course'], eno)

        self.__cur.execute(SQL, values)
        self.__conn.commit()

    def select_data(self):
        SQL = "SELECT * FROM stud"
        self.__cur.execute(SQL)
        rows = self.__cur.fetchall()
        for row in rows:
            print(row)

    def __del__(self):
        self.__cur.close()
        self.__conn.close()


if __name__ == '__main__':
    db = Crud_Op()
    # db.insert_data('Harshit', 72, 7049530992, 'harshitdalal96@gmail.com', 'MCA')
    # db.insert_data('mayank', 100, 7067601202, 'maynak12@gmail.com', 'MCA')
    # db.update_data(2, s_name="Mayank")
    # db.update_data(2, email="mayank.shrikhande1607@gmail.com")
    # db.delete_data(2)
    db.select_data()
