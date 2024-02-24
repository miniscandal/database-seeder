class DatabaseStatementExecute():
    def __init__(self, cursor_execute) -> None:
        self.cursor_execute = cursor_execute

    def foreign_key_check(self, check: bool):
        statement = f"SET foreign_key_checks = {check}"
        self.cursor_execute(statement, None)

    def drop_database(self, name: str) -> None:
        statement = f"DROP DATABASE IF EXISTS {name}"
        self.cursor_execute(statement, None)

    def create_database(self, name: str) -> None:
        statement = f"CREATE DATABASE IF NOT EXISTS {name}"
        self.cursor_execute(statement, None)

    def use_database(self, name: str) -> None:
        statement = f"USE {name}"
        self.cursor_execute(statement, None)

    def create_table(self, name: str, columns: list, constraints: list) -> None:
        columns_str = ', '.join(columns)
        constraints_str = ', '.join(constraints)
        definition = columns_str
        if constraints:
            definition = f"{columns_str}, {constraints_str}"
        statement = f"CREATE TABLE IF NOT EXISTS {name} ({definition}) ENGINE = InnoDB"
        self.cursor_execute(statement, None)

    def insert_into(self, table_name: str, records: list) -> None:
        for record in records:
            columns = ', '.join(record.keys())
            placeholders = ', '.join(['%s'] * len(record))
            statement = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            values = tuple(record.values())
            self.cursor_execute(statement, values)
