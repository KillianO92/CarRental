import tkinter as RETK
#from tkinter import messagebox
from CustDBFunctions import *
from CarsDBFunctions import *
from ResDBFunctions import *
from BaseDBFunctions import *
from CustFunctions import *

cstDB = CustDBFunctions()
carDB = CarsDBFunctions()
resDB = ResDBFunctions()
baseDB = BaseDBFunctions()

class ResEditDialog(object):
    root = None

    def __init__(self, parent):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        
        self.top = RETK.Toplevel(ResEditDialog.root)
        self.frm = RETK.Frame(self.top, borderwidth=4, relief='ridge')
        self.frm.pack(fill='both', expand=True)

        self.resID = parent.resID

        self.output = resDB.loadRealRes(self.resID)

        self.carID = self.output[0][1]
        self.custID = self.output[0][2]
        self.sDate = self.output[0][3]
        self.eDate = self.output[0][4]
        self.rsDate = self.output[0][5]
        self.reDate = self.output [0][5]



        self.label = RETK.Label(self.frm, text="Editing Reservation: {} starting on {} and ending on {}".format(self.resID, self.sDate, self.eDate))
        self.label.pack(padx=4, pady=4)

        self.customer_value = RETK.StringVar()
        self.cbCars = RETK.Label(self.frm, text='List of Cars')
        self.cbCars.pack(padx=4, pady=4)

        self.cbMakes = RETK.ttk.Combobox(self.frm, textvariable=self.customer_value, width=50, state="readonly")
        self.cbMakes['values'] = carDB.loadAllCars()
        self.cbMakes.pack(pady=4, padx=4)
        self.cbMakes.set(carDB.loadCarsByID(self.carID))

        self.lblsDate = RETK.Label(self.frm, text='Start Date')
        self.lblsDate.pack(padx=4, pady=4)
        self.entrysDate = RETK.Entry(self.frm)
        self.entrysDate.pack(pady=4, padx=4)
        self.entrysDate.insert(0, '{}'.format(self.sDate))


        self.lbleDate = RETK.Label(self.frm, text = 'End Date')
        self.lbleDate.pack(padx=4, pady=4)
        self.entryeDate = RETK.Entry(self.frm)
        self.entryeDate.pack(pady=4, padx=4)
        self.entryeDate.insert(0, '{}'.format(self.eDate))

        self.lblrsDate = RETK.Label(self.frm, text = 'Real Start Date')
        self.lblrsDate.pack(padx=4, pady=4)
        self.entryrsDate = RETK.Entry(self.frm)
        self.entryrsDate.pack(pady=4, padx=4)
        self.entryrsDate.insert(0, '{}'.format(self.rsDate))

        self.lblreDate = RETK.Label(self.frm, text = 'Real End Date')
        self.lblreDate.pack(padx=4, pady=4)
        self.entryreDate = RETK.Entry(self.frm)
        self.entryreDate.pack(pady=4, padx=4)
        self.entryreDate.insert(0, '{}'.format(self.reDate))

        self.b_cancel = RETK.Button(self.frm, text='Cancel')
        self.b_cancel['command'] = self.top.destroy
        self.b_cancel.pack(padx=4, pady=4)    

        self.b_OK = RETK.Button(self.frm, text='OK')
        self.b_OK['command'] = self.updateRes
        self.b_OK.pack(padx=4, pady=4)


    def updateRes(self):
        print("Updating the Reservation in the databse....")
        cusString = str(self.customer_value.get()).strip('{}')
        car = carDB.loadCarsByID(self.carID)
        carString = '{} {} {}'.format(car[0][0], car[0][1], car[0][2])

        if cusString != carString:
            self.carID = self.customer_value.get()
            spacePos = cusString.find(' ')
            self.carID = cusString[0:spacePos]
            print("this is inside if {}:".format(self.carID))
        else:
            self.carID = self.output[0][1]
        
        
        StartDate = self.entrysDate.get()
        EndDate = self.entryeDate.get()
        RealStartDate = self.entryrsDate.get()
        RealEndDate = self.entryreDate.get()
        ReservationID = self.resID
        print('carid: {}\nsdate: {}\nedate:{}\nrsdate:{}\nredate:{}'.format(self.carID, StartDate, EndDate, RealStartDate, RealEndDate))
        resDB.UpdateReservation(ReservationID, self.carID, StartDate, EndDate, RealStartDate, RealEndDate)

        
        

        



