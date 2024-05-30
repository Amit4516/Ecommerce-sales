import os

import pandas as pd
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
host = os.getenv('HOST')
username = os.getenv('USER')
passsword = os.getenv('PASSWORD')

connection = mysql.connector.connect(host=host,
                                     user=username,
                                     password=passsword,
                                     database='swiftmarket')

cursor = connection.cursor()

def querytodataframe(query):


    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df

def showtables():
    query = """SHOW TABLES;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(data=rows,columns=cursor.column_names)
    return df

def describetable(tablename):
    query = f"""Describe {tablename};"""
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.dataframe(data=rows,columns=cursor.column_names)
    return df