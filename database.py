#connecting to MSSQL
import pyodbc 
from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

connection_string = f'DRIVER=SQL Server;SERVER=LDDEVDTG1SQLDC1;'
connection_string += f'DATABASE=Logging;'
connection_string += f'TRUSTED_CONNECTION=yes'

connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string})  

engine = create_engine(connection_url)               

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#print(engine.table_names())


