from faker import Faker
from shared.normal_classes.database_statement_execute.feature import DatabaseStatementExecute
from shared.functions.db_routines import new_database
from shared.functions.db_routines import insert_fake_records
from feature_db_authorized_cell_phone_dealer.entities.user import User
from feature_db_authorized_cell_phone_dealer.entities.employee import Employee
from feature_db_authorized_cell_phone_dealer.entities.employee_position import EmployeePosition


def start_authorized_cell_phone_dealer(db_statement_execute: DatabaseStatementExecute) -> None:
    database_name = 'authorized_cell_phone_dealer'
    new_database(db_statement_execute, database_name)
    user_sequence = [
        {
            'name': 'Evie',
            'employee_id': 1
        },
        {
            'name': 'Igna',
            'employee_id': 2
        },
        {
            'name': 'Komi',
            'employee_id': 3
        }
    ]
    insert_fake_records(db_statement_execute, User(Faker(), 3, user_sequence))

    employee_sequence = [
        {
            'employee_position_id': '1'
        },
        {
            'employee_position_id': '2'
        },
        {
            'employee_position_id': '3'
        }
    ]
    insert_fake_records(db_statement_execute, Employee(Faker(), 3, employee_sequence))

    employee_position_sequence = [
        {
            'name': 'administrator warranty'
        },
        {
            'name': 'promoter'
        },
        {
            'name': 'manager'
        }
    ]
    insert_fake_records(db_statement_execute, EmployeePosition(Faker(), 5))
