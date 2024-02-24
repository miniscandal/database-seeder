from shared.abstract_classes.entity import Entity


class Employee(Entity):
    _name = 'employees'

    column_definition = {
        'employee_id': 'INT NOT NULL AUTO_INCREMENT',
        'name': 'VARCHAR(255)',
        'email': 'VARCHAR(255)',
        'employee_position_id': 'INT NOT NULL'
    }

    constraint_definition = {
        'foreign_key': [{
            'entity': 'employee_positions',
            'primary_key': 'employee_position_id'
        }]
    }

    primary_key = 'employee_id'

    def generate_fake_data(self) -> dict:
        return {
            'name': self.fake.name(),
            'email': self.fake.email(),
            'employee_position_id': 1
        }
