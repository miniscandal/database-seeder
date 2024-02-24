from .entity import Entity


class CellPhone(Entity):
    name = 'cell_phones'

    attributes = {
        'cell_phone_id': 'INT NOT NULL AUTO_INCREMENT',
        'imei': 'VARCHAR(255)',
        'fabricante': 'VARCHAR(255)',
        'modelo': 'VARCHAR(255)'
    }

    column_definition = {
        'PRIMARY KEY': 'cell_phone'
    }

    def generate_fake_data(self) -> dict:
        '''
        :return: dic with fake data
        '''
        return {
            'imei': self.fake.random_number(digits=15, fix_len=True)
        }
