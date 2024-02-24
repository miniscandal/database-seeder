from abc import ABC, abstractmethod


class Entity(ABC):
    _name = ''
    column_definition = {}
    constraint_definition = {}
    primary_key = ''
    count = 0
    sequence = []

    def __init__(self, fake, count: int, sequence: list = []) -> None:
        self.fake = fake
        self.count = count
        self._insert_pk_in_column_definition()
        self.sequence = sequence

    @abstractmethod
    def generate_fake_data(self):
        '''
        :return: dict with fake data.
        '''
        pass

    def _insert_pk_in_column_definition(self):
        definition = self.column_definition[self.primary_key]
        self.column_definition[self.primary_key] = f"{definition} PRIMARY KEY"

    @property
    def name(self) -> str:
        '''
        :return: str representing the name of the entity.
        '''
        return self._name

    def insert_sequence(self, index, record) -> tuple:
        keys = self.sequence[index].keys()

        for key in keys:
            record[key] = self.sequence[index][key]

        if index < len(self.sequence) - 1:
            index = index + 1
        else:
            index = 0

        return record, index

    def generate_fake_records(self, count: int) -> list:
        '''
        :return: List with fake records to insert into the database.
        '''
        fake_records = []
        index = 0
        for _ in range(count):
            record = self.generate_fake_data()
            if len(self.sequence):
                record, index = self.insert_sequence(index, record)
            fake_records.append(record)
            print(record)

        return fake_records

    def generate_column_definition(self) -> list:
        '''
        :return: list with colums for entity in database.
        '''

        attributes_list = [f"{key} {value}" for key, value in self.column_definition.items()]

        return attributes_list

    def generate_contraint_definition(self) -> list:
        '''
        :return: list with contraint definitions for entity in database
        '''
        constraint_definitions = []
        for fk in self.constraint_definition['foreign_key']:
            delete = 'ON DELETE CASCADE'
            update = 'ON UPDATE RESTRICT'
            entity = fk['entity']
            primary_key = fk['primary_key']
            foreing_key = f"FOREIGN KEY ({primary_key}) REFERENCES {entity} ({primary_key})"
            constraint = f"CONSTRAINT `fk_{self.name}_{entity}` {foreing_key} {delete} {update}"
            constraint_definitions.append(constraint)

        return constraint_definitions
