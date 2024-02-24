from .entity import Entity


class Promotor(Entity):
    name = 'promotor'

    attributes = {
        'promotor_id': 'INT NOT NULL AUTO_INCREMENT',
        'store_id': 'VARCHAR(255)'
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
