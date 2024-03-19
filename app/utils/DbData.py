import pymssql
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


try:
    conn = pymssql.connect(
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PWD"),
        server=os.getenv("DB_SERVER"),
        database=os.getenv("DB_DATABASE"),
    )
except pymssql.Error as e:
    print("Error connecting to Azure SQL Database:", e)


def db_load(conn, DbTable):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM Cv.{DbTable}")
    DbData = cursor.fetchall()
    ColNams = [desc[0] for desc in cursor.description]
    DfData = pd.DataFrame(DbData, columns=ColNams)
    cursor.close()
    return DfData


Cv = db_load(conn=conn, DbTable="Cv")
Hobbies = db_load(conn=conn, DbTable="Hobbies")
Pensum = db_load(conn=conn, DbTable="Pensum")
Interests = db_load(conn=conn, DbTable="Interests")
Interests

conn.close()
