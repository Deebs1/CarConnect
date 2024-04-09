import pyodbc
import sys
# from DatabaseConnectionError import DatabaseConnectionError 
# from DatabaseConnectionHandling import DatabaseConnectionError
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/util")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/dao")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/entity")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/exception")
from db_property_util import DBPropertyUtil
class db_conn_util:
    def getConnection():
        try:
            connection_string = DBPropertyUtil.get_connection_string()
            connection = pyodbc.connect(connection_string)
            print("Connected Successfully")
            return connection

        except pyodbc.Error  as e:
            print("Error connecting to the database:", e)
