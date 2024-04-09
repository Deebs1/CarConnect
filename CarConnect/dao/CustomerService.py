import sys
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/util")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/dao")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/entity")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/exception")

from db_conn_util import db_conn_util
from ICustomerService import ICustomerService
from Customer import Customer
from CustomerNotFoundException import CustomerNotFoundException



def get_connection():
    return db_conn_util.getConnection()


'''
def close_connection(cursor, connection):
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
'''


class CustomerService(ICustomerService):

    def get_customer_by_id(self, customer_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Customer WHERE customer_id = ?", (customer_id,))
            customer_data = cursor.fetchone()

            if not customer_data:
                raise CustomerNotFoundException("Customer with ID {} not found".format(customer_id))

            customer = Customer(*customer_data)
            return customer

        except Exception as e:
            print("Error:", e)
            return None

    def get_customer_by_username(self, username):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Customer WHERE username = ?", (username,))
            customer_data = cursor.fetchone()

            if not customer_data:
                raise CustomerNotFoundException("Customer with username {} not found".format(username))

            customer = Customer(*customer_data)
            return customer

        except Exception as e:
            print("Error:", e)
            return None



    def register_customer(self, customer):
        try:
            connection = get_connection()  # Assuming get_connection() returns a valid pyodbc connection
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Customer (customer_id, first_name, last_name, email, phone_number, address, username,"
                "password, registration_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (customer.get_customer_id(), customer.get_first_name(), customer.get_last_name(), customer.get_email(),
                customer.get_phone_number(), customer.get_address(), customer.get_username(),
                customer.get_password(), customer.get_registration_date()))

            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False


    def update_customer(self, customer):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE Customer SET first_name=?, last_name=?, email=?, phone_number=?, address=?, "
                "username=?, password=?, registration_date=? WHERE customer_id=?",
                (customer.get_first_name(), customer.get_last_name(), customer.get_email(), customer.get_phone_number(),
                customer.get_address(), customer.get_username(), customer.get_password(),
                customer.get_registration_date(), customer.get_customer_id()))
            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def delete_customer(self, customer_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Customer WHERE customer_id=?", (customer_id,))
            connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False
