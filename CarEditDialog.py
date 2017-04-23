import tkinter as CARTK
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

class CarEditDialog(object):
    root = None

    def __init__(self, parent):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """

    
        self.top = CARTK.Toplevel(CarEditDialog.root)
        self.frm = CARTK.Frame(self.top, borderwidth=4, relief='ridge')
        self.frm.pack(fill='both', expand=True)

        self.carID = parent.carID

        output = carDB.loadCarsByID(self.carID)
        self.make = output[0][0]
        self.model = output[0][1]
        self.color = output[0][2]



        self.label = CARTK.Label(self.frm, text="Editing: {} {} {}".format(self.color, self.make, self.model))
        self.label.pack(padx=4, pady=4)

        self.lblMake = CARTK.Label(self.frm, text=self.make)
        self.lblMake.pack(padx=4, pady=4)


        self.lblModel = CARTK.Label(self.frm, text = 'Model')
        self.lblModel.pack(padx=4, pady=4)
        self.entryModel = CARTK.Entry(self.frm)
        self.entryModel.pack(pady=4, padx=4)
        self.entryModel.insert(0, self.model)

        self.lblColor = CARTK.Label(self.frm, text = 'Color')
        self.lblColor.pack(padx=4, pady=4)
        self.entryColor = CARTK.Entry(self.frm)
        self.entryColor.pack(pady=4, padx=4)
        self.entryColor.insert(0, self.color)

        self.b_cancel = CARTK.Button(self.frm, text='Cancel')
        self.b_cancel['command'] = self.top.destroy
        self.b_cancel.pack(padx=4, pady=4)    

        self.b_OK = CARTK.Button(self.frm, text='OK')
        self.b_OK['command'] = self.UpdateAndClose
        self.b_OK.pack(padx=4, pady=4)

##        self.btnReload = CARTK.Button(self.frm, text='Reload Customers')
##        self.btnReload['command'] = self.reload
##        self.btnReload.pack(padx=4, pady=4)
##
##    def reload(self):
##        cstFun.Reload()

    def popup(self):
        self.win = CARTK.Toplevel()
        self.win.wm_title("No Changes")

        self.lblNo = CARTK.Label(self.win, text="There were no changes made\n\n")
        self.lblNo.grid(row=0, column=0)


        self.btnOK = CARTK.ttk.Button(self.win, text="Okay", command=self.win.destroy)
        self.btnOK.grid(row=1, column=0)

    def popup2(self):
        self.win = CARTK.Toplevel()
        self.win.wm_title("Changes")

        self.lblNo = CARTK.Label(self.win, text="Changes Were Committed\n\n")
        self.lblNo.grid(row=0, column=0)


        self.btnOK = CARTK.ttk.Button(self.win, text="Okay", command=self.win.destroy)
        self.btnOK.grid(row=1, column=0)
        
        

    def updateCar(self):
        Model = self.entryModel.get()
        Color = self.entryColor.get()
        CarID = self.carID
        
        if Model != self.model or Color != self.color:
            carDB.UpdateCar(Model, Color, CarID)
            self.popup2()
        else:
            self.popup()


    def close(self):
        self.top.wait_window(self.win)
        self.top.destroy()

    def UpdateAndClose(self):
        self.updateCar()
        self.close()

        
        

        



