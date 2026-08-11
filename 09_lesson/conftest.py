import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import StaticPool

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/DZ_Final"

engine = create_engine(
    DATABASE_URL,
    poolclass=StaticPool,
    connect_args=(
        {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
    ),
)

TestingSessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


@pytest.fixture(scope="function")
def db_session():
    """
    Создает новую сессию БД для каждого теста.
    Оборачивает действия теста во вложенную транзакцию, которая откатывается в конце.
    """
    connection = engine.connect()
    transaction = connection.begin_nested()

    session = TestingSessionLocal(bind=connection)

    @pytest.fixture(autouse=True)
    def cleanup():
        yield
        session.close()
        transaction.rollback()
        connection.close()

    return session
