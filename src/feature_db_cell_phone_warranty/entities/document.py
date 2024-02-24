from shared.abstract_classes.entity import Entity


class Document(Entity):
    _name = 'documents'

    column_definition = {
        'document_id': 'INT NOT NULL AUTO_INCREMENT'
    }

    constraint_definition = {
        'foreign_key': []
    }

    primary_key = 'document_id'

    def generate_fake_data(self) -> dict:
        '''
        :return: dict with fake data.
        '''
        return {
        }
