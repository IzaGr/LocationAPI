from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database.mydatabase import MyDatabase
import pytest


@pytest.fixture(scope='session')
def engine():
    return create_engine('sqlite://database.db')


@pytest.yield_fixture(scope='session')
def tables(engine):
    MyDatabase.metadata.create_all(engine)
    yield
    MyDatabase.metadata.drop_all(engine)


@pytest.yield_fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()