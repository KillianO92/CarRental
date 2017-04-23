import tkinter as NVTK
#from tkinter import messagebox
from CustDBFunctions import *
from CarsDBFunctions import *
from ResDBFunctions import *
from BaseDBFunctions import *
from CustFunctions import *
from ast import literal_eval

cstDB = CustDBFunctions()
carDB = CarsDBFunctions()
resDB = ResDBFunctions()
baseDB = BaseDBFunctions()

class NewVehicleDialog(object):
    root = None

    def MakeSelected(self, event):
        print("You have the selected Make n")
        make = self.make_value.get()
        spacePos = make.find(' ')
        MakeID = make[0:spacePos]
        self.cbModels['values'] = carDB.loadCarModels(MakeID)


    def __init__(self):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        
        self.top = NVTK.Toplevel(NewVehicleDialog.root)
        self.frm = NVTK.Frame(self.top, borderwidth=4, relief='ridge')
        self.frm.pack(fill='both', expand=True)

        self.label = NVTK.Label(self.frm, text="Add New Vehicle")
        self.label.pack(padx=4, pady=4)

        self.lblMake = NVTK.Label(self.frm, text='Make')
        self.lblMake.pack(padx=4, pady=4)

        self.make_value = NVTK.StringVar()
        self.cbMakes = NVTK.ttk.Combobox(self.frm, textvariable=self.make_value, width=50, state="readonly")
        self.cbMakes['values'] = carDB.loadCarMakes()
        self.cbMakes.bind("<<ComboboxSelected>>", self.MakeSelected)
        self.cbMakes.pack(pady=4, padx=4)


        #TODO make it so once make is selected it changes MakeID
        make = self.make_value.get()
        spacePos = make.find(' ')
        MakeID = make[0:spacePos]

        self.lblModel = NVTK.Label(self.frm, text = 'Model')
        self.lblModel.pack(padx=4, pady=4)

        self.model_value = NVTK.StringVar()
        self.cbModels = NVTK.ttk.Combobox(self.frm, textvariable=self.model_value, width=50, state="readonly")
        if (MakeID == ''):
            for dat in self.cbModels.get():
                self.cbModels.set('')
        else:
            self.cbModels['values'] = carDB.loadCarModels(MakeID)
        self.cbModels.pack(pady=4, padx=4)

        self.lblModelNew = NVTK.Label(self.frm, text="If Model not present input here")
        self.lblModelNew.pack(padx=4, pady=4)
        self.entryModel = NVTK.Entry(self.frm)
        self.entryModel.pack(pady=4, padx=4)
        

        self.lblColor = NVTK.Label(self.frm, text = 'Color')
        self.lblColor.pack(padx=4, pady=4)
        self.entryColor = NVTK.Entry(self.frm)
        self.entryColor.pack(pady=4, padx=4)

        self.b_cancel = NVTK.Button(self.frm, text='Cancel')
        self.b_cancel['command'] = self.top.destroy
        self.b_cancel.pack(padx=4, pady=4)    

        self.b_OK = NVTK.Button(self.frm, text='OK')
        self.b_OK['command'] = self.addVehicle
        self.b_OK.pack(padx=4, pady=4)

        
    def modelPopup(self):
        self.win = NVTK.Toplevel()
        self.win.wm_title("Error")

        self.lblEmpty = NVTK.Label(self.win, text="   ")
        self.lblEmpty.grid(row=0, column=0)
        
        self.lblNo = NVTK.Label(self.win, text="No Valid Model\n\n")
        self.lblNo.grid(row=0, column=1)

        self.lblEmpty2 = NVTK.Label(self.win, text="   ")
        self.lblEmpty2.grid(row=0, column=2)

        self.btnOK = NVTK.ttk.Button(self.win, text="Okay", command=self.win.destroy)
        self.btnOK.grid(row=1, column=1)
        


    def addVehicle(self):
        print("Adding the Vehicle into the databse....")
        make = self.make_value.get()
        spacePos = make.find(' ')
        MakeID = make[0:spacePos]
        if self.model_value.get() == '' and self.entryModel.get() == '':
            self.modelPopup()
        elif self.model_value.get() == '':
            Model = self.entryModel.get()            
        else:
            Model = self.cbModels.get()
            
        Color = self.entryColor.get()

        carDB.AddVehicle(self.MakeID, Model, Color)

 
