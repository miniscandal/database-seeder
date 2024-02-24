class DBMSConnect:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBMSConnect, cls).__new__(cls)
        return cls._instance

    def __init__(self, sys, driver, db_credentials: dict) -> None:
        """
        :param sys: A module that provides functions and variables that are used
         to manipulate different parts of the Python runtime environment.
        :param driver: The database driver to use for the connection.
        :param db_credentials: A dictionary containing database credentials.
         Must include 'user', 'password' and 'host'.
        :return: None
        """
        self.sys = sys
        self.driver = driver
        self.db_credentials = db_credentials
        self.error = self.driver.Error
        self.connection = self.connect_database()
        self.cursor = self.connection.cursor()

    def connect_database(self) -> any:
        """
        :return: connection for database management system.
        """
        user = self.db_credentials["user"]
        password = self.db_credentials["password"]
        host = self.db_credentials["host"]
        connection = None
        try:
            connection = self.driver.connect(user=user, password=password, host=host)
        except self.error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            self.sys.exit(1)

        return connection

    def cursor_execute(self, statement: str, data) -> bool:
        """
        param statement: A string that represents the SQL statement to be executed.
        param data: The data to use in the SQL statement.
        :return: True if the execution is successful or false if the execution is unsuccessful.
        """
        successful = None
        try:
            self.cursor.execute(statement, data)
            successful = True
        except self.error as e:
            self.cursor.close()
            print(f"Error: {e}")
            successful = False

        return successful

    def connect_close(self) -> None:
        self.connection.commit()
        self.connection.close()
