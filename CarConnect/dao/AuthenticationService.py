import sys
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/util")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/dao")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/entity")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/exception")

from db_conn_util import db_conn_util

from AuthenticationException import AuthenticationException


def get_connection():
    return db_conn_util.getConnection()


class AuthenticationService:
    def authenticate_customer(self, username, password):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Customer WHERE username = ? AND password = ?", (username, password))
            customer_data = cursor.fetchone()

            if not customer_data:
                raise AuthenticationException("Incorrect Username or Password...")

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def authenticate_admin(self, username, password):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Admin WHERE username = ? AND password = ?", (username, password))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AuthenticationException("Incorrect Username or Password...")

            return True

        except Exception as e:
            print("Error:", e)
            return False
