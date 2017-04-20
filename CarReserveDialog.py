#TODO:  Find out why the import names must be unique
import tkinter as CRTK
from CustDBFunctions import *
from CarsDBFunctions import *
from ResDBFunctions import *

cstDB = CustDBFunctions()
carDB = CarsDBFunctions()
resDB = ResDBFunctions()

class CarReserveDialog(object):
    root = None

    def __init__(self, parent):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        #self.tki = CRTK.Tk()
        self.top = CRTK.Toplevel(CarReserveDialog.root)
        self.CarRentedEvent = CRTK.Event
        self.frm = CRTK.Frame(self.top, borderwidth=4, relief='ridge')
        self.frm.pack(fill='both', expand=True)

        self.carID = parent.carID
        output = carDB.loadCarsByID(self.carID)
        for dat in output:
            string = '{} {} {}'.format(dat[2], dat[0], dat[1])


        self.label = CRTK.Label(self.frm, text="Reserving Vehicle: {}".format(string))
        self.label.pack(padx=4, pady=4)

        self.lblCust = CRTK.Label(self.frm, text="Select the Customer Renting the Car")
        self.lblCust.pack(padx=4, pady=4)

        #TODO:  Add Combo Box or List Box of Customers to Select from....
        self.customer_value = CRTK.StringVar()
        self.cbpMakes = CRTK.ttk.Labelframe(self.frm, text='List of Car Makes')
        self.cbMakes = CRTK.ttk.Combobox(self.frm, textvariable=self.customer_value, width=50)
        #add the handler to capture when the selected value is changed
        #self.cbMakes.bind("<<ComboboxSelected>>", self.model_selected )
        self.cbMakes['values'] = cstDB.loadCustomers()
        self.cbMakes.pack(pady=4, padx=4)
        #self.cbMakes.location(x=0, y=0)

        self.lblStart = CRTK.Label(self.frm, text='Start Date')
        self.lblStart.pack(padx=4, pady=4)
        self.entryStart = CRTK.Entry(self.frm)
        self.entryStart.pack(pady=4, padx=4)
        self.entryStart.insert(0, 'YYYY-MM-DD')

        self.lblEnd = CRTK.Label(self.frm, text = 'End Date')
        self.lblEnd.pack(padx=4, pady=4)
        self.entryEnd = CRTK.Entry(self.frm)
        self.entryEnd.pack(pady=4, padx=4)
        self.entryEnd.insert(0, 'YYYY-MM-DD')

        self.b_cancel = CRTK.Button(self.frm, text='Cancel')
        self.b_cancel['command'] = self.top.destroy
        self.b_cancel.pack(padx=4, pady=4)    

        self.b_OK = CRTK.Button(self.frm, text='OK')
        self.b_OK['command'] = self.rentCar
        #self.b_OK['command'] = self.top.destroy
        self.b_OK.pack(padx=4, pady=4) 

    def rentCar(self):
        print("Insert the Row into the databse....")
        cus = self.customer_value.get()
        spacePos = cus.find(' ')
        custID= cus[0:spacePos]
        sDate = self.entryStart.get()
        eDate = self.entryEnd.get()
        #TODO Figure out why it isn't going to DB
        print(self.carID ,custID, sDate, eDate)
        resDB.AddNewReservation(self.carID, custID, sDate, eDate)

        



