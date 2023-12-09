from icecream import ic
from database import Database


class Operations:

    def __init__(self, tg_id: int, operation_amount: float, category_id: int, as_name: str, type_operation: int):
        self.tg_id = tg_id
        self.operation_amount = operation_amount
        self.category_id = category_id
        self.as_name = as_name
        self.type_operation = type_operation

    # Подключение к БД
    def db_connect(self):
        return Database()
    
    # расход
    def add_expense(self):
        db = self.db_connect()

        with db as conn:
            # вызов процедуры insert_operation
            query = 'CALL insert_operation (%s, %s, %s, %s, %s);'

            user_params = (self.tg_id, self.operation_amount, self.category_id, self.as_name, self.type_operation)
            result = conn.execute_query(query, user_params)
            return result

    # пополнение
    def add_income(self):
        db = self.db_connect()

        with db as conn:
            # вызов процедуры insert_operation
            query = 'CALL insert_operation (%s, %s, %s, %s, 1);'

            user_params = (self.tg_id, self.operation_amount, self.category_id, self.as_name)
            result = conn.execute_query(query, user_params)
            return result
            
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

tg_id = 12349
operation_amount = 1011.0 
category_id = 5 
as_name = "Товары для дома"
type_operation = 2

operations_instance = Operations(tg_id=tg_id, operation_amount=operation_amount, category_id=category_id, as_name=as_name, type_operation=type_operation)
ic(operations_instance.add_expense())