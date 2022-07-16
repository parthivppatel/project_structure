from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./my_app.db"postgresql://postgres:postgres@localhost:5432/postgres
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL ,connect_args={"check_same_thread": False}
)
# engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres", pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
