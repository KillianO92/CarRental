import BaseDBFunctions as db

#Class for handling the Car Inventory
class CarsDBFunctions(db.BaseDBFunctions):
    #instantiate class and BaseDBFunctions
    def __init__(self):
        super().__init__()

    def loadAllCars(self):
        records = super().loadRecords("SELECT C.CarID , M.Make , C.Model , C.Doors , C.Color , ( SELECT COUNT(1) FROM Reservations AS R WHERE R.CarID = C.CarID AND ( ( DATETIME(R.EndDate) > DATETIME('now') ) OR ( DATETIME(R.RealStartDate) <= DATETIME('now') AND R.RealEndDate IS NULL ) ) ) AS IsRented FROM MAKES AS M INNER JOIN CARS AS C ON M.MakeID = C.MakeID ORDER BY M.Make , C.Model")
        return records

    def loadCarsByMake(self, make):
        records = super().loadRecords("SELECT C.CarID, M.Make, C.Model, C.Doors FROM MAKES AS M INNER JOIN CARS AS C ON M.MakeID = C.MakeID WHERE M.MAKE = '{}' ORDER BY M.Make, C.Model".format(make))
        return records

    def loadCarsByModel(self, model):
        records = super().loadRecords("SELECT C.CarID, M.Make, C.Model, C.Doors FROM MAKES AS M INNER JOIN CARS AS C ON M.MakeID = C.MakeID WHERE M.MODEL = '{}' ORDER BY M.Make, C.Model".format(model))
        return records

    def loadCarsByID(self, carID):
        records = super().loadRecords("SELECT M.Make, C.Model, C.Color FROM MAKES AS M INNER JOIN CARS AS C ON M.MakeID = C.MakeID WHERE C.CarID = '{}'".format(carID))
        return records

    def UpdateCar(self, Model, Color, CarID):
        super().AddNewRecord("UPDATE Cars Set Model = '{}', Color = '{}' WHERE CarID = '{}'".format(Model, Color, CarID))

    def loadCarMakes(self):
        records = super().loadRecords("Select * from Makes ORDER BY MakeID")
        return records

    def loadCarModels(self, MakeID):
        records = super().loadRecords("Select Model from CARS as C INNER JOIN MAKES as M ON C.MakeID = M.MakeID WHERE M.MakeID = {}".format(MakeID))
        return records

    def AddVehicle(self, MakeID, Model, Color):
        super().AddNewRecord("INSERT INTO Cars Set MakeID ='{}', Model = '{}', Color = '{}'".format(MakeID, Model, Color))
