import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

DATABASE_URL = "postgresql+psycopg2://postgres:123@localhost:5432/DZ_Final"

# Фабрика создается один раз при импорте модуля. 
# Она не хранит состояние (как scoped_session), а просто умеет делать новые сессии.
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False)

engine = create_engine(
    DATABASE_URL,
    # StaticPool нужен только для SQLite :memory:. Для PostgreSQL его лучше убрать или задать условие.
    poolclass=StaticPool if "sqlite" in DATABASE_URL else None,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin_nested()
    session = sessionmaker(bind=connection)()
    yield session
    session.close()
    transaction.rollback()
    connection.close()
    