from icecream import ic

class Operations:

    def __init__(self, db):
        self.db = db

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
    def check_balance(self, user_id):
        pass
    
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