
import tkinter
import os # needed for relative image paths
class Main(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('Capture.GIF', file = os.path.dirname(__file__) + '/Capture.GIF'))
        self._images.append(tkinter.PhotoImage('Capture1.GIF', file = os.path.dirname(__file__) + '/Capture1.GIF'))


        # Widget Initialization
        self._label_1 = tkinter.Label(root, activebackground = "#b3a88e", background = "#b3a88e", font = "{MV Boli} 21", text = "WELCOME TO CAB BOOKING",)
        self._label_2 = tkinter.Label(root, activebackground = "#999999",background = "#999999",font = "{MS Sans Serif} 12 bold", text = "from", )
        self.fromspinner = tkinter.Spinbox(root, font = "{MS Sans Serif} 10", to = 5,values = "block-1 GH-5 GH-6 GH=1 GH-2", )
        self._label_3 = tkinter.Label(root, activebackground = "#cccccc",background = "#cccccc",font = "{MS Sans Serif} 12 bold",text = "destination",)
        self.destinationspinner = tkinter.Spinbox(root, to = 5, values = "block1 gh1 gh2 gh3 gh6",)
        self._label_4 = tkinter.Label(root,activebackground = "#bcbcbc",background = "#bcbcbc",font = "{MS Sans Serif} 12 bold",text = "date", )
        self._label_6 = tkinter.Label(root,activebackground = "#999999", background = "#999999", font = "{MS Sans Serif} 12 bold", text = "fare", )
        self._label_7 = tkinter.Label(root,activebackground = "#999999", background = "#999999",  font = "{MS Sans Serif} 12 bold",  takefocus = 1, text = "payment mode", )
        self._entry_1 = tkinter.Entry(root,width = 0,)
        self.fare = tkinter.Label(root,font = "{MS Sans Serif} 10 bold",foreground = "#ff0000", text = 0.0,)
        self._radiobutton_2 = tkinter.Radiobutton(root, image = "Capture.GIF",text = "_radiobutton_2",)
        self._label_9 = tkinter.Label(root, activebackground = "#cccccc",background = "#cccccc",font = "{MS Sans Serif} 13 bold",text = "Name",)
        self.name = tkinter.Entry(root,width = 0,)
        self._radiobutton_3 = tkinter.Radiobutton(root,font = "{MS UI Gothic} 12 bold",text = "Pay by cash",)
        self._radiobutton_4 = tkinter.Radiobutton(root,image = "Capture1.GIF",text = "_radiobutton_4",)
        self._button_1 = tkinter.Button(root,font = "{MS Sans Serif} 12 bold",text = "submit",)

        # widget commands

        self.fromspinner.configure(command = self.fromspinner_command)
        self.fromspinner.configure(invalidcommand = self.fromspinner_invalidcommand)
        self.fromspinner.configure(validatecommand = self.fromspinner_validatecommand)
        self.fromspinner.configure(xscrollcommand = self.fromspinner_xscrollcommand)
        self.destinationspinner.configure(command = self.destinationspinner_command)
        self.destinationspinner.configure(invalidcommand = self.destinationspinner_invalidcommand)
        self.destinationspinner.configure(validatecommand = self.destinationspinner_validatecommand)
        self.destinationspinner.configure(scrollcommand = self.destinationspinner_xscrollcommand)
        self._entry_1.configure(invalidcommand = self._entry_1_invalidcommand)
        self._entry_1.configure(validatecommand = self._entry_1_validatecommand)
        self._entry_1.configure(xscrollcommand = self._entry_1_xscrollcommand)
        self._radiobutton_2.configure(command = self._radiobutton_2_command)
        self.name.configure(invalidcommand = self.name_invalidcommand)
        self.name.configure(validatecommand = self.name_validatecommand)
        self.name.configure(xscrollcommand = self.name_xscrollcommand)
        self._radiobutton_3.configure(command = self._radiobutton_3_command)
        self._radiobutton_4.configure(command = self._radiobutton_4_command)
        self._button_1.configure(command = self._button_1_command)


        # Geometry Management
        self._label_1.grid(in_    = root,column = 1,row    = 1,columnspan = 4,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_2.grid(in_    = root,column = 1,row    = 3,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.fromspinner.grid(in_    = root,column = 2,row    = 3,columnspan = 3,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_3.grid(in_    = root,column = 1,row    = 4,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.destinationspinner.grid(in_    = root,column = 2,row    = 4,columnspan = 3,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_4.grid(in_    = root,column = 1,row    = 5,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_6.grid(in_    = root,column = 1,row    = 6,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_7.grid(in_    = root,column = 1,row    = 7,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._entry_1.grid(in_    = root,column = 2,row    = 5,columnspan = 3,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.fare.grid(in_    = root,column = 2,row    = 6,columnspan = 3,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._radiobutton_2.grid(in_    = root,column = 3,row    = 7,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._label_9.grid(in_    = root,column = 1,row    = 2,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self.name.grid(in_    = root,column = 2,row    = 2,columnspan = 3,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._radiobutton_3.grid(in_    = root,column = 4,row    = 7,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._radiobutton_4.grid(in_    = root,column = 2,row    = 7,columnspan = 1,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")
        self._button_1.grid(in_    = root,column = 1,row    = 8,columnspan = 4,padx = 0,ipady = 0,pady = 0,rowspan = 1,sticky = "nsew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(4, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(5, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(6, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(7, weight = 1, minsize = 40, pad = 0)
        root.grid_rowconfigure(8, weight = 0, minsize = 65, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 152, pad = 0)
        root.grid_columnconfigure(2, weight = 0, minsize = 152, pad = 0)
        root.grid_columnconfigure(3, weight = 0, minsize = 106, pad = 0)
        root.grid_columnconfigure(4, weight = 0, minsize = 99, pad = 0)


