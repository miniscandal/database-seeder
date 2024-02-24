from faker import Faker
from shared.normal_classes.database_statement_execute.feature import DatabaseStatementExecute
from shared.functions.db_routines import new_database
from shared.functions.db_routines import insert_fake_records
from feature_db_cell_phone_warranty.entities.document import Document


def start_cell_phone_warranty(db_statement_execute: DatabaseStatementExecute) -> None:
    database_name = 'cell_phone_warranty'
    new_database(db_statement_execute, database_name)
    insert_fake_records(db_statement_execute, Document(Faker(), 3))
