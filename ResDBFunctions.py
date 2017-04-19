import BaseDBFunctions as db

#Class for handling the Car Inventory
class ResDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()

    def loadAllRes(self):
        records = super().loadRecords("SELECT * FROM Reservations")
        return records

    def loadResByFName(self, fName):
        records = super().loadRecords("".format(fName))
        return records

    def loadResbyLName(self, lName):
        records = super().loadRecords("".format(lName))
        return records

    def DeleteReservation(self, reservationID):
        super().loadRecords("DELETE FROM Reservations WHERE ReservationID = '{}'".format(reservationID))
