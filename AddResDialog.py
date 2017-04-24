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

class AddResDialog(object):
    root = None

    def __init__(self, parent):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        
        self.top = RETK.Toplevel(AddResDialog.root)
        self.frm = RETK.Frame(self.top, borderwidth=4, relief='ridge')
        self.frm.pack(fill='both', expand=True)

        self.custID = parent.custID
        self.sDate = parent.sDate
        self.eDate = parent.eDate

        custName = cstDB.loadCustomerName(self.custID)



        self.label = RETK.Label(self.frm, text="Making Reservation For: {} starting on {} and ending on {}".format(custName, self.sDate, self.eDate))
        self.label.pack(padx=4, pady=4)

        self.customer_value = RETK.StringVar()
        self.cbCars = RETK.Label(self.frm, text='List of Cars')
        self.cbCars.pack(padx=4, pady=4)

        self.cbMakes = RETK.ttk.Combobox(self.frm, textvariable=self.customer_value, width=50, state="readonly")
        self.cbMakes['values'] = carDB.loadAllCars()
        self.cbMakes.pack(pady=4, padx=4)

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
        #print('carid: {}\nsdate: {}\nedate:{}\nrsdate:{}\nredate:{}'.format(self.carID, StartDate, EndDate, RealStartDate, RealEndDate))
        #resDB.UpdateReservation(ReservationID, self.carID, StartDate, EndDate, RealStartDate, RealEndDate)

        
        

        



