import tkinter
import os # needed for relative image paths
class Aboutus(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('about-us (1).gif', file = os.path.dirname(__file__) + '/about-us (1).gif'))


        # Widget Initialization
        self._labelframe_1 = tkinter.LabelFrame(root,background = "#f1fd60",font = "{Lucida Sans Unicode} 8 bold",text = "License",)
        self._label_4 = tkinter.Label(root,activebackground = "#ffffff",background = "#ffffff",borderwidth = 0,image = "about-us (1).gif",text = "_label_4",)
        self._label_5 = tkinter.Label(root,activebackground = "#fcff7d",background = "#fcff7d",borderwidth = 0,font = "{MS Sans Serif} 10 bold",
                                      text = """Cab Booking designed by Gurjeet, Parnasree,Shubham, Anmol.
                                            \uD83D\uDC8C Email ID - pujadas2481@gmail.com
                                            \uD83D\uDCDE Phone number - +917973277319
                                             \uD83C\uDF10 Whats app - +917973277319
                                                 """)

        # Geometry Management
        self._labelframe_1.grid(in_    = root,column = 1, row    = 3, columnspan = 1, ipadx = 0, ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._label_4.grid(in_    = root,column = 1, row    = 1, columnspan = 1, ipadx = 0, ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._label_5.grid(in_    = root,column = 1, row    = 2, columnspan = 1, ipadx = 0, ipady = 0,padx = 0,pady = 0,rowspan = 1,sticky = "news")
        self._label_1.grid(in_    = root,column = 1, row    = 1, columnspan = 1, ipadx = 0, ipady = 0,padx = 0,pady = 0,rowspan = 3,sticky = "news")

        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 155, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 5, pad = 0)
        self._labelframe_1.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._labelframe_1.grid_rowconfigure(2, weight = 0, minsize = 40, pad = 0)
        self._labelframe_1.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        self._labelframe_1.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)


