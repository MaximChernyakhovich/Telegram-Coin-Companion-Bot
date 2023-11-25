from icecream import ic
from database import Database

class User:
    def __init__(self, tg_id: int, firstname: str, lastname: str, tg_nick: str):
        self.tg_id = tg_id
        self.firstname = firstname
        self.lastname = lastname
        self.tg_nick = tg_nick

    # Подключение к БД
    def db_connect(self):
        return Database()

    def __str__(self):
        return f"User ID: {self.tg_id}\nName: {self.firstname} {self.lastname}\nUsername: {self.tg_nick}"

    def create_profile(self):
        pass

    def fetch_user(self):
        db = self.db_connect()

        with db as conn:

            # проверка наличия пользователя в БД
            check_id = db.fetch_data('''WITH local_id AS (
                                            SELECT %s
                                        )
                                        SELECT 
                                            CASE 
                                                WHEN EXISTS (
                                                    SELECT "ID" 
                                                    FROM users 
                                                    WHERE "ID" = (SELECT * 
                                                                    FROM local_id)) 
                                                THEN 1
                                                ELSE 0
                                            END''', 
                                            (self.tg_id,))[0]

            if check_id[0] != 0:
                data = db.fetch_data('''SELECT * 
                                        FROM users 
                                        WHERE "ID" = %s''', (self.tg_id,))[0]
                return data
            else:
                # здесь будет выполняться функция create_profile для добавления пользователя в БД
                pass



user = User(tg_id=12345, firstname="Ivan", lastname="Ivanov", tg_nick="ivanivanov")

user_data = user.fetch_user()
print(user_data)
