import pyodbc

class DBPropertyUtil:
    def get_connection_string():
   
        connection_string =  "DRIVER={SQL Server};SERVER=LAPTOP-4T7CQ1UB\SQLEXPRESS;" \
                             "DATABASE=CarConnect;Trusted_Connection=yes;"
        return connection_string