from sqlalchemy import create_engine, text
from app import db  # import your Flask SQLAlchemy db instance
from app.models import Author, BookAuthor, Book, BookCategory, Category, User

# Step 1 – Connect to 'master' and create the database
engine_master = create_engine(
    "mssql+pyodbc://sa:YourStrong!Pass123@db/master?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine_master.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
    conn.execute(text("""
    IF NOT EXISTS (
        SELECT name FROM sys.databases WHERE name = 'OnlineLibraryDB'
    )
    EXEC('CREATE DATABASE OnlineLibraryDB')
    """))

# Step 2 – Connect to 'OnlineLibraryDB' and create tables
db_engine = create_engine(
    "mssql+pyodbc://sa:YourStrong!Pass123@db/OnlineLibraryDB?driver=ODBC+Driver+17+for+SQL+Server"
)
db.metadata.create_all(db_engine)
