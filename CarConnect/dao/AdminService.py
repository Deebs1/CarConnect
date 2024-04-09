import sys
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/util")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/dao")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/entity")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/exception")
# sys.path.append("C:/Users/kathir/OneDrive/Desktop/key/python/CarConnect/util")
# sys.path.append("C:/Users/kathir/OneDrive/Desktop/key/python/CarConnect/dao")
# sys.path.append("C:/Users/kathir/OneDrive/Desktop/key/python/CarConnect/entity")
# sys.path.append("C:/Users/kathir/OneDrive/Desktop/key/python/CarConnect/exception")
from db_conn_util import db_conn_util
from IAdminService import IAdminService
from Admin import Admin
from AdminNotFoundException import AdminNotFoundException
from InvalidInputException import InvalidInputException


def get_connection():
    return db_conn_util.getConnection()

class AdminService(IAdminService):

    def get_admin_by_id(self, admin_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Admin WHERE adminID = ?", (admin_id,))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AdminNotFoundException("Admin with ID {} not found".format(admin_id))

            admin = Admin(*admin_data)
            return str(admin)

        except InvalidInputException:
            print("Required field is missing or has an incorrect format")

        except Exception as e:
            print("Error:", e)
            return None

    def get_admin_by_username(self, username):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Admin WHERE Username = ?", (username,))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AdminNotFoundException("Admin with username {} not found".format(username))

            admin = Admin(*admin_data)
            return admin

        except InvalidInputException:
            print("Required field is missing or has an incorrect format")

        except Exception as e:
            print("Error:", e)
            return None

    def register_admin(self, admin):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Admin (adminID, firstName, lastName, email, phoneNumber, username, password, role, joinDate) VALUES (?,?,?,?,?,?,?,?,?)",
                (admin.get_adminID(), admin.get_firstName(), admin.get_lastName(), admin.get_email(),
                admin.get_phoneNumber(), admin.get_username(), admin.get_password(), admin.get_role(),
                admin.get_joinDate()))

            connection.commit()

            return True

        except InvalidInputException:
            print("Required field is missing or has an incorrect format")

        except Exception as e:
            print("Error:", e)
            return False

    def update_admin(self, admin: Admin):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE Admin SET firstName=?, lastName=?, email=?, phoneNumber=?, username=?, password=?, role=?, joinDate=? WHERE adminID=?",
                (admin.get_firstName(), admin.get_lastName(), admin.get_email(), admin.get_phoneNumber(),
                admin.get_username(), admin.get_password(), admin.get_role(), admin.get_joinDate(), admin.get_adminID()))

            connection.commit()
            return True

        except Exception as e:
            print("Error updating admin:", e)
            return False

    def delete_admin(self, admin_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Admin WHERE adminID=?", (admin_id,))
            connection.commit()
            return True

        except Exception as e:
            print("Error deleting admin:", e)
            return False