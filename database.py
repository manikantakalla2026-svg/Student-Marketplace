from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database
DATABASE_URL = "sqlite:///./student_marketplace.db"

# create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class
Base = declarative_base()
