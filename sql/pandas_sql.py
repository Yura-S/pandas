import pandas as pd
from sqlalchemy import create_engine
import os
# import numpy
# import pyodbc
# import sqlalchemy

####################################################EXTRACT FROM DATABASE#######################################################
######################################################ADDING VARIABLES FOR CONNECTIO STRING
db_address = 'localhost' # HOME-PC
db_name = 'AdventureWorks2016'
#db_port = '1433'
#db_username = ''
#db_password = ''

######################################################CREATING CONNECTION
def mssql_engine():
    cnx = 'mssql+pyodbc://' + db_address + '/' + db_name + '?driver=SQL+Server+Native+Client+11.0'
    engine = create_engine(cnx)
    return engine

######################################################SOME SQL QUERIES
# query = 'SELECT * FROM INFORMATION_SCHEMA.TABLES'
query = 'SELECT top 100 * FROM Person.Person'
# query = 'SELECT DB_NAME()'

######################################################EXTRACT FROM TABLE TO VARIABLE
df = pd.read_sql(query, mssql_engine() )

######################################################SORTING EXAMPLE
df = df.sort_values(by='BusinessEntityID', ascending=False)

######################################################BEFORE CREATING FILE FROM EXTRACT CHECK.IF FILE EXISTS DELETE IT 
print(os.path.dirname(os.path.abspath(__file__)))

if os.path.exists('./sql/table.xlsx'):
    os.remove("./sql/table.xlsx")
if os.path.exists('./sql/table.csv'):
    os.remove("./sql/table.csv")
if os.path.exists('./sql/table.json'):
    os.remove("./sql/table.json")
if os.path.exists('./sql/table.txt'):
    os.remove("./sql/table.txt")            

######################################################ADD DATA TO FILES
df.to_excel('./sql/table.xlsx')
df.to_csv('./sql/table.csv')
df.to_json('./sql/table.json')
df.to_string('./sql/table.txt')