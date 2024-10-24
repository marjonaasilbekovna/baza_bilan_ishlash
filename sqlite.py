# import sqlite3

# class Database:
#     def __init__(self, path_to_db="users.db"):
#         # Bazaga ulanish
#         self.connection = sqlite3.connect(path_to_db)
#         self.cursor = self.connection.cursor()

#     def execute(self, sql, parameters=None, commit=False):
#         if parameters is None:
#             parameters = ()
        # self.cursor.execute(sql, parameters)
        # if commit:
        #     self.connection.commit()

#     def create_table_users(self):
#         # Users jadvalini yaratamiz
#         sql = """
#         CREATE TABLE IF NOT EXISTS Users(
#             name TEXT,
#             surname TEXT,
#             age INTEGER,
#             tel TEXT,
#             kurs TEXT
#         );
#         """
#         self.execute(sql, commit=True)

#     def add_user(self, name: str, surname: str, age: int, tel: str, kurs: str):
#         # Foydalanuvchini jadvalga qo'shamiz
#         sql = """
#         INSERT INTO Users(name, surname, age, tel, kurs) VALUES(?, ?, ?, ?, ?);
#         """
#         self.execute(sql, parameters=(name, surname, age, tel, kurs), commit=True)

#     def close(self):
#         # Bazani yopamiz
#         self.connection.close()


import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()

    def execute(self, sql, parameters=None, commit=False):
        if parameters is None:
            parameters = ()
        self.cursor.execute(sql, parameters)
        if commit:
            self.connection.commit()

    def create_table_users(self):
        # Users jadvalini yaratish
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            full_name TEXT,
            name TEXT,
            surname TEXT,
            age INTEGER,
            phone TEXT,
            course TEXT,
            region TEXT,
            district TEXT
        )
        """
        self.execute(sql, commit=True)

    def add_user(self, telegram_id, full_name, name, surname, age, phone, course, region, district):
        # Foydalanuvchini jadvalga qo'shish
        sql = """
        INSERT OR IGNORE INTO users (telegram_id, full_name, name, surname, age, phone, course, region, district)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(telegram_id, full_name, name, surname, age, phone, course, region, district), commit=True)

    def get_user_count(self):
        # Barcha foydalanuvchilarni sanaydi
        self.cursor.execute("SELECT COUNT(*) FROM users")
        count = self.cursor.fetchone()[0]
        return count

    def close(self):
        # Bazani yopamiz
        self.connection.close()
