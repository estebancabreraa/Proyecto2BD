import psycopg2
from psycopg2 import Error
"""
Conexion en computadora de Raul Monzon:
        user = "postgres",
        password = "raul1998",
        host = "127.0.0.1",
        port = "5433",
        database = "BDPROYECTO2"
"""
try:
    
    connection = psycopg2.connect(user = "postgres",
                                  password = "raul1998",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "BDPROYECTO2")
    cursor = connection.cursor()
    
    create_table_query = '''CREATE TABLE mobile
          (ID INT PRIMARY KEY     NOT NULL,
          MODEL           TEXT    NOT NULL,
          PRICE         REAL); '''
    
    cursor.execute(create_table_query)
    
    connection.commit()
    
    print("Table created successfully in PostgreSQL ")
except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
