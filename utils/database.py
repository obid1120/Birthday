import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_staff(self, f_name, l_name, image, birthday, position):
        # print(f_name, l_name, image, birthday)
        self.cursor.execute(
            "Insert into staff (f_name, l_name, image, birthday, position) values (?, ?, ?, ?, ?)",
            (f_name, l_name, image, birthday, position)
        )
        self.conn.commit()

    def get_staff(self):
        staffs = self.cursor.execute(
            "select f_name, l_name, image, birthday, position from staff"
        )
        return staffs.fetchall()

    def add_tg_id(self, tg_id):
        self.cursor.execute(
            "insert into user_id (tg_id) values (?)", (tg_id, )
        )
        self.conn.commit()

    def get_tg_id(self):
        tg_id = self.cursor.execute(
            "select tg_id from user_id"
        )
        return tg_id.fetchall()