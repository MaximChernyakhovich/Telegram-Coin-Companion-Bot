from icecream import ic
from database import Database


class Operations:

    def __init__(self, tg_id: int):
        self.tg_id = tg_id

    # Подключение к БД
    def db_connect(self):
        return Database()
    
    # расход
    def add_expense(self, user_id, amount, category):
        pass

    # пополнение
    def add_income(self, user_id, amount, source):
        pass
    
    # список последних транзакций
    def last_transactions(self, user_id):
        pass

    # проверка баланса
    def check_balance(self):

        db = self.db_connect()

        with db as conn:
            # вызов процедуры add_user
            data = db.fetch_data('''
                                 select money_amount 
                                    from balance
                                    where user_id = %s;''', (self.tg_id,))[0][0]
            return data
    
    # вывод статистики за месяц
    def get_statistics(self, user_id, month):
        pass

    # вывод статистики за месяц
    def view_stats(self, user_id, month):
        pass

    # добавление каьегории
    def add_category(self, user_id, category):
        pass
    
    # изменение категории
    def change_category (self, user_id, category):
        pass
    
    # удаление категории
    def del_category (self, user_id, category):
        pass
    
    # вывод краткого списка часто используемых комментариев 
    # пользователя чтобы не вводить текст с клавиатуры
    def user_comments (self, user_id):
        pass

op = Operations(tg_id=12349)

balance = op.check_balance()
ic(balance)