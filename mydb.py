"""
    Install MySQL on your computer
    https://dev.mysql.com/downloads/installer/
    pip install mysql
    pip install mysql-connector
    pip install mysql-connector-python
"""

import os
import mysql.connector

from dotenv import load_dotenv

# load .env file
load_dotenv()

# get environment variables
NAME = os.getenv("NAME")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
PORT = os.getenv("PORT")

# connect to database

dataBase = mysql.connector.connect(
    host=HOST, user=USER, password=PASSWORD, port=int(PORT)
)

# prepare a cursor object using cursor() method
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute(f"CREATE DATABASE {NAME}")

dataBase.close()

print("Database created successfully")
