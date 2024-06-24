from settings import settings
from sqlalchemy import create_engine
from models import Base, LinkAccess
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
 
# создание движка
engine = create_engine(SQLALCHEMY_DATABASE_URL)
new_session = sessionmaker(autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine, tables=[LinkAccess.__table__])