# src/database.py
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./agenda.db"

# connect_args={"check_same_thread": False} es requerido solo para SQLite
engine = create_engine(DATABASE_URL, echo=False, connect_args={"check_same_thread": False})

def create_db_and_tables():
    """Crea las tablas definidas si no existen al iniciar la app."""
    SQLModel.metadata.create_all(engine)

def get_session():
    """Generador de sesión inyectable mediante Depends() de FastAPI."""
    with Session(engine) as session:
        yield session
