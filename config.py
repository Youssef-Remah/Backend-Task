"""
This file:

-Initializes DB configuration keys
"""
import os

class Config:
    SECRET_KEY = 'super-secret-key'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = os.getenv(
    'SQLALCHEMY_DATABASE_URI',
    # Fallback to your Windows Auth connection
    "mssql+pyodbc://@DESKTOP-5BI4L12/OnlineLibraryDB?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "trusted_connection=yes"
    )
