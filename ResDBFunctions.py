import BaseDBFunctions as db

#Class for handling the Car Inventory
class ResDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()

    def loadAllRes(self):
        records = super().loadRecords("SELECT * FROM Reservations")
        return records

    def loadResByID(self, custID):
        records = super().loadRecords("Select * FROM Reservations WHERE CustomerID = '{}'".format(custID))
        return records

    def loadResBySDate(self,sDate):
        records = super().loadRecords("SELECT * FROM Reservations WHERE StartDate = '{}'".format(sDate))
        return records

    def loadResByEDate(self,eDate):
        records = super().loadRecords("SELECT * FROM Reservations WHERE EndDate = '{}'".format(eDate))
        return records

    def loadResByDates(self,sDate, eDate):
        records = super().loadRecords("SELECT * FROM Reservations WHERE StartDate = '{}' AND EndDate = '{}'".format(sDate, eDate))
        return records
    def loadResByAll(self,custID, sDate, eDate):
        records = super().loadRecords("SELECT * FROM Reservations WHERE CustomerID = '{}' AND StartDate = '{}' AND EndDate = '{}'".format(custID, sDate, eDate))
        return records

    def DeleteReservation(self, reservationID):
        super().loadRecords("DELETE FROM Reservations WHERE ReservationID = '{}'".format(reservationID))
