import os
from contextlib import contextmanager
from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
