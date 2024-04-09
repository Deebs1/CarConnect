import sys

sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/util")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/dao")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/entity")
sys.path.append("C:/Users/deebi/OneDrive/Desktop/CarConnect/CarConnect/exception")
from db_conn_util import db_conn_util
from IReservationService import IReservationService
from Reservation import Reservation
from ReservationException import ReservationException

def get_connection():
    return db_conn_util.getConnection()
class ReservationService(IReservationService):
    def get_reservation_by_id(self, reservationID):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE reservationID = ?", (reservationID,))
            reservation_data = cursor.fetchone()

            if not reservation_data:
                raise ReservationException("Reservation with ID {} not found".format(reservationID))

            reservation = Reservation(*reservation_data)
            return reservation

        except Exception as e:
            print("Error:", e)
            return None

    def get_reservations_by_customer_id(self, customer_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE customerID = ?", (customer_id,))
            reservation_data = cursor.fetchall()

            if not reservation_data:
                raise ReservationException("No reservations found for customer with ID {}".format(customer_id))

            reservations = []
            for row in reservation_data:
                reservation = Reservation(*row)
                reservations.append(reservation)

            return reservations

        except Exception as e:
            print("Error:", e)
            return None

    def create_reservation(self, reservation):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Reservation (reservationID, customerID, vehicleID, startDate, EndDate, TotalCost, Status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (reservation.get_reservationID(), reservation.get_customerID(), reservation.get_vehicleID(),
                reservation.get_startDate(), reservation.get_endDate(), reservation.get_totalCost(),
                reservation.get_status()))

            connection.commit()
            print("Reservation Created!!")
            return True

        except Exception as e:
            print("Error:", e)
            return False

    def update_reservation(self, reservation):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE Reservation SET customerID=?, vehicleID=?, startDate=?, endDate=?, TotalCost=?, Status=? WHERE reservationID=?",
                (reservation.get_customerID(), reservation.get_vehicleID(), reservation.get_startDate(),
                reservation.get_endDate(), reservation.get_totalCost(), reservation.get_status(),
                reservation.get_reservationID()))

            connection.commit()
            print("Reservation Updated!!")
            return True

        except Exception as e:
            print("Error:", e)
            return False

    def cancel_reservation(self, reservation_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Reservation WHERE reservationID=?", (reservation_id,))
            connection.commit()
            print("Reservation Cancelled!!")
            return True

        except Exception as e:
            print("Error:", e)
            return False