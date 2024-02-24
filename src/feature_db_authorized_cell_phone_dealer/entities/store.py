from .entity import Entity


class Store(Entity):
    name = 'store'

    attributes = {
        'store_id': 'INT NOT NULL AUTO_INCREMENT',
        'gerente_id': 'INT NOT NULL',
        'address': 'VARCHAR(255)',
        'created_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP',
        'updated_at': 'TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
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
