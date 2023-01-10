from .db_connect import Connection


class ERPTable(Connection):

    def insert_data(self, fullname, email, phone, pos, address, dob, company) -> None:
        sql = "INSERT INTO erp(fullname, email, phone, pos, address, dob, company) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (fullname, email, phone, pos, address, dob, company)

        self._cur.execute(sql, values)

    def delete_data(self, eid: int) -> None:
        sql = "DELETE FROM erp WHERE eid = %s"
        value = eid

        self._cur.execute(sql, value)

    def update_data(self, eid: int, fullname, email, phone, pos, address, dob, company) -> None:
        sql = "UPDATE erp SET fullname = %s, email = %s, phone = %s, pos = %s, address = %s, dob = %s, company = %s " \
              "WHERE eid = %s"
        values = (fullname, email, phone, pos, address, dob, company, eid)
        self._cur.execute(sql, values)

    def select_by_id(self, *eid) -> list:
        sql = "SELECT * FROM erp WHERE eid = %s"
        value = eid
        self._cur.execute(sql, value)
        row = self._cur.fetchone()
        return row

    def select_all(self) -> list:
        sql = "SELECT * FROM erp ORDER BY eid ASC"
        self._cur.execute(sql)
        rows = self._cur.fetchall()
        return rows
