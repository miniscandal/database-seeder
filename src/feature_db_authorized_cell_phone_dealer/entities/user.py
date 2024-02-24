from shared.abstract_classes.entity import Entity
import random


class User(Entity):
    _name = 'users'

    column_definition = {
        'user_id': 'INT NOT NULL AUTO_INCREMENT',
        'name': 'VARCHAR(50) NOT NULL',
        'password': 'VARCHAR(255)',
        'employee_id': 'INT NOT NULL'
    }

    constraint_definition = {
        'foreign_key': [{
            'entity': 'employees',
            'primary_key': 'employee_id'
        }]
    }

    primary_key = 'user_id'

    def generate_fake_data(self) -> dict:
        return {
            'name': self.fake.name(),
            'password': self.fake.password(),
            'employee_id': self.fake.random_int(min=5, max=100)
        }
