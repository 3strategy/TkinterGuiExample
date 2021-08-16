import pandas as pd
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TWS\SQLEXPRESS;'
                      'Database=Nathalie_Library;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

sql_query = pd.read_sql_query('SELECT * FROM Nathalie_Library.dbo.authors',conn)
print(sql_query)
print(type(sql_query))