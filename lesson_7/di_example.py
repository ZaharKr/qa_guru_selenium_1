"""
Простейший пример Dependency Injection (из материалов занятия).

ResourceManager не создаёт connection сам — получает снаружи (инъекция).
В тестах подставляем mock вместо реального DBConnection.
"""


class DBConnection:
    def connect(self):
        raise NotImplementedError("реальная БД в unit-тесте не нужна")

    def update_database(self):
        raise NotImplementedError("реальная БД в unit-тесте не нужна")


class ResourceManager:
    def __init__(self, connection=None):
        self.connection = connection

    def set_db_connection(self, connection):
        self.connection = connection

    def update(self, connection=None):
        if connection is not None:
            self.connection = connection
        self.connection.connect()
        self.connection.update_database()
        return True
