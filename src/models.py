from utils.database import db


class BaseModel:
    """ Базовая модель для работы с БД """

    # Название таблицы в БД
    table_name = None

    def __init__(self):
        self._connection = db.connection

    @property
    def connection(self):
        return self._connection

    def get_list(self):
        """ Возвращает список всех записей из таблицы """

        query = f"""
            SELECT * FROM {self.table_name}
        """
        result = self.connection.execute(query).fetchall()
        return [dict(row) for row in result]

    def get_by_id(self, id: int):
        """ Возвращает запись по её ID """
        query = f"""
            SELECT * FROM {self.table_name} WHERE id = ?
        """
        values = (id,)
        result = self.connection.execute(query, values).fetchone()
        return dict(result) if result is not None else None

    def get_by_field(self, field_name, value):
        """Возвращает запись по значению поля field_name"""
        query = f"""
            SELECT * FROM {self.table_name} WHERE {field_name} = ?
        """
        values = (value,)
        result = self.connection.execute(query, values).fetchone()
        return dict(result) if result is not None else None

    def create(self, attributes: dict):
        """ Создаёт запись в таблице """

        # Выбираем все поля из словаря
        field_names = attributes.keys()
        # Выбираем все значения из словаря
        # Сразу преобразуем в tuple для записи
        field_values = tuple(attributes.values())
        # Создаём шаблон со всеми названиями полей для SQL запроса
        keys_placeholder = ','.join(field_names)
        # Создаём шаблон ?,?,? по кол-ву значений полей для SQL запроса
        values_placeholder = ('?,' * len(field_values)).rstrip(',')
        query = f"""
            INSERT INTO {self.table_name} ({keys_placeholder}) 
            VALUES ({values_placeholder})
        """
        cursor = self.connection.execute(query, field_values)
        self.connection.commit()
        # Возвращаем ID последней добавленой записи
        return cursor.lastrowid

    def update(self, id: int, attributes: dict):
        """ Изменяет запись в таблице """

        field_names = attributes.keys()
        field_values = tuple(attributes.values()) + (id,)
        placeholder = " = ?, ".join(field_names) + " = ?"

        query = f"""UPDATE {self.table_name} SET {placeholder} WHERE id = ?"""

        cursor = self.connection.execute(query, field_values)
        self.connection.commit()

        return cursor.lastrowid

    def delete(self, id: int):
        """ Удаляет запись в таблице """

        query = f"""DELETE FROM {self.table_name} WHERE id = ?"""
        values = (id,)

        self.connection.execute(query, values)

        self.connection.commit()


class UserModel(BaseModel):
    """
        Класс конкретной модели, представляющий собой таблицу пользователей
        Наследуется от BaseModel
    """

    table_name = 'users'


class CategoriesModel(BaseModel):
    """
        Таблица категорий
    """

    table_name = 'categories'
