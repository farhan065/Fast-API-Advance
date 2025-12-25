# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.main import app, get_db
from app.config import settings

# 1. SETUP TEST DATABASE URL
# Use a specific test database to avoid deleting your real data
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. THE FIXTURE (Runs before EVERY test function)
@pytest.fixture()
def session():
    # A. Setup: Drop old tables and create new ones (Empty DB)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    # B. Create a new session for the test
    db = TestingSessionLocal()
    
    # C. Dependency Override: Force app to use this test session
    try:
        yield db
    finally:
        db.close()

# 3. CLIENT FIXTURE (Makes it easy to use in tests)
from fastapi.testclient import TestClient

@pytest.fixture()
def client(session): # <--- This requests the 'session' fixture above
    # Override the get_db dependency with the one created in step 2
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
            
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
