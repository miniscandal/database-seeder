import os
import sys
import mariadb
from dotenv import load_dotenv
from shared.normal_classes.dbms_connect.feature import DBMSConnect
from shared.normal_classes.database_statement_execute.feature import (
    DatabaseStatementExecute,
)
from feature_db_authorized_cell_phone_dealer.feature import (
    start_authorized_cell_phone_dealer,
)
from feature_db_cell_phone_warranty.feature import start_cell_phone_warranty


load_dotenv()


def get_db_credentials(os) -> dict:
    """
    :return: dict with credentials for database management system
    """
    db_credentials = {
        "user": os.getenv("DB_USERNAME"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
    }
    return db_credentials


def main():
    db_credentials = get_db_credentials(os)
    dbms_connect = DBMSConnect(sys=sys, driver=mariadb, db_credentials=db_credentials)
    db_statement_execute = DatabaseStatementExecute(dbms_connect.cursor_execute)
    db_statement_execute.foreign_key_check(False)
    start_authorized_cell_phone_dealer(db_statement_execute)
    # start_cell_phone_warranty(db_statement_execute)
    db_statement_execute.foreign_key_check(True)
    dbms_connect.connect_close()


if __name__ == "__main__":
    main()


# astroid==3.0.1
# black==23.12.0
# click==8.1.7
# colorama==0.4.6
# dill==0.3.7
# Faker==20.1.0
# isort==5.12.0
# mariadb==1.1.8
# mccabe==0.7.0
# mypy-extensions==1.0.0
# packaging==23.2
# pathspec==0.12.1
# platformdirs==4.0.0
# python-dateutil==2.8.2
# python-dotenv==1.0.0
# six==1.16.0
# tomlkit==0.12.3
