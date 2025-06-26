"""
This file:

-Initializes DB configuration keys
"""
import os

class Config:
    SECRET_KEY = 'super-secret-key'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@DESKTOP-5BI4L12/OnlineLibraryDB?driver=ODBC%20Driver%2017%20for%20SQL%20Server&trusted_connection=yes"
    )
