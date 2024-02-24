from shared.abstract_classes.entity import Entity


def new_database(db_statement_execute, db_database) -> None:
    db_statement_execute.drop_database(db_database)
    db_statement_execute.create_database(db_database)
    db_statement_execute.use_database(db_database)


def insert_fake_records(db_statement_execute, entity: Entity) -> None:
    column_definition = entity.generate_column_definition()
    constraint_definition = entity.generate_contraint_definition()
    fake_records = entity.generate_fake_records(entity.count)
    db_statement_execute.create_table(entity.name, column_definition, constraint_definition)
    db_statement_execute.insert_into(entity.name, fake_records)
