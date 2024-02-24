from shared.abstract_classes.entity import Entity


class EmployeePosition(Entity):
    _name = 'employee_positions'

    column_definition = {
        'employee_position_id': 'INT NOT NULL AUTO_INCREMENT',
        'name': 'VARCHAR(50) NOT NULL'
    }

    constraint_definition = {
        'foreign_key': []
    }

    primary_key = 'employee_position_id'

    def generate_fake_data(self) -> dict:
        return {
            'name': self.fake.name()
        }
