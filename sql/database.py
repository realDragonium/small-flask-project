import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


url: str = os.environ.get("DB_URL",  "localhost:10432")
username: str = os.environ.get("DB_USER",  "DONT_LEAVE_ME_ALONE")
password: str = os.environ.get("DB_PASS",  "CHANGE_ME")


engine = create_engine(f"postgresql://{username}:{password}@{url}", pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)

