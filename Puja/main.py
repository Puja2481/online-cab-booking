from tkcalendar import DateEntry
import tkinter
import os  # needed for relative image paths
from tkinter import *
from main_ui import *
from tkinter import messagebox
import random
import string
via = ""
class Main(object):
    _images = []  # Holds image refs to prevent GC
    fromindex = 0
    destinationindex = 0

    def setprice(self, *args):
        global via
        print("You have selected " + str(self.var.get()))
        via = str(self.var.get())
        price = [[0, 10, 20, 30, 40, 50], [10, 0, 10, 20, 30, 40], [20, 10, 0, 10, 20, 30], [30, 20, 10, 0, 10, 20],
                 [40, 30, 20, 10, 0, 10], [50, 40, 30, 20, 10, 0]]
        destination = ["Block-1", "GH-1", "GH-2", "GH-3", "GH-5", "GH-6"]
        fromp = ["Block-1", "GH-1", "GH-2", "GH-3", "GH-5", "GH-6"]

        for i in fromp:
            if (str(self.fromspinner.get()) == i):
                fromindex = fromp.index(i)

        for j in destination:
            if (str(self.destinationspinner.get()) == j):
                destinationindex = destination.index(j)

        self.fare["text"] = str(price[fromindex][destinationindex]) + " rs"
        pass

    def __init__(self, root):
        self.var = IntVar()
        self._images.append(tkinter.PhotoImage('Capture.GIF', file=os.path.dirname(__file__) + '/Capture.GIF'))
        self._images.append(tkinter.PhotoImage('Capture1.GIF', file=os.path.dirname(__file__) + '/Capture1.GIF'))

        # Widget Initialization
        self._label_1 = tkinter.Label(root,activebackground="#b3a88e",background="#b3a88e",font="{MV Boli} 21",text="WELCOME TO CAB BOOKING",)
        self._label_2 = tkinter.Label(root,activebackground="#999999",background="#999999",font="{MS Sans Serif} 12 bold",text="from",)
        self.fromspinner = tkinter.Spinbox(root,font="{MS Sans Serif} 15",to=6,values="Block-1 GH-1 GH-2 GH-3 GH-5 GH-6",)
        self._label_3 = tkinter.Label(root,activebackground="#cccccc",background="#cccccc",font="{MS Sans Serif} 12 bold",text="destination",)
        self.destinationspinner = tkinter.Spinbox(root,font="{MS Sans Serif} 15",to=6,values="Block-1 GH-1 GH-2 GH-3 GH-5 GH-6",)
        self._label_4 = tkinter.Label(root,activebackground="#bcbcbc",background="#bcbcbc",font="{MS Sans Serif} 12 bold",text="date",)
        self._label_6 = tkinter.Label(root,activebackground="#999999",background="#999999",font="{MS Sans Serif} 12 bold",text="fare",)
        self._label_7 = tkinter.Label(root, activebackground="#999999",background="#999999",font="{MS Sans Serif} 12 bold",takefocus=1,text="payment mode",)
        self._entry_1 = DateEntry(root, width=12, font="{MS Sans Serif} 15", background='darkblue', foreground='white', borderwidth=2, year=2019)
        self.fare = tkinter.Label(root, font="{MS Sans Serif} 10 bold",foreground="#ff0000",text=0.0, )
        self._label_9 = tkinter.Label(root, activebackground="#cccccc", background="#cccccc",font="{MS Sans Serif} 13 bold",text="Name",)
        self.name = tkinter.Entry(root, font="{MS Sans Serif} 13", width=0,)
        self._radiobutton_2 = tkinter.Radiobutton(root,image="Capture.GIF",text="UPI",  value=2,variable=self.var,command=self.setprice )
        self._radiobutton_3 = tkinter.Radiobutton(root, font="{MS UI Gothic} 12 bold", value=3, text="Pay by cash", command=self.setprice, variable=self.var,)
        self._radiobutton_4 = tkinter.Radiobutton(root,value=1,image="Capture1.GIF", variable=self.var,command=self.setprice, text="Paytm",)
        self._button_1 = tkinter.Button(root,font="{MS Sans Serif} 12 bold",text="submit",)

        # widget commands

        self._button_1.configure(command=self._button_1_command)

        # Geometry Management
        self._label_1.grid(in_=root,column=1,row=1,columnspan=4,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._label_2.grid(in_=root,column=1,row=3,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self.fromspinner.grid(in_=root,column=2,row=3,columnspan=3,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._label_3.grid(in_=root,column=1,row=4,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self.destinationspinner.grid(in_=root,column=2,row=4,columnspan=3,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._label_4.grid(in_=root,column=1,row=5,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._label_6.grid(in_=root,column=1,row=6,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._label_7.grid(in_=root,column=1,row=7,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._entry_1.grid(in_=root,column=2,row=5,columnspan=3,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self.fare.grid(in_=root,column=2,row=6,columnspan=3,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._radiobutton_2.grid(in_=root,column=3,row=7,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._label_9.grid(in_=root,column=1,row=2,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self.name.grid(in_=root,column=2,row=2,columnspan=3,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._radiobutton_3.grid(in_=root,column=4,row=7,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._radiobutton_4.grid(in_=root,column=2,row=7,columnspan=1,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")
        self._button_1.grid(in_=root,column=1,row=8,columnspan=4,ipadx=0, ipady=0, padx=0, pady=0,rowspan=1,sticky="nsew")

        # Resize Behavior
        root.grid_rowconfigure(1, weight=0, minsize=40, pad=0)
        root.grid_rowconfigure(2, weight=0, minsize=40, pad=0)
        root.grid_rowconfigure(3, weight=0, minsize=40, pad=0)
        root.grid_rowconfigure(4, weight=0, minsize=40, pad=0)
        root.grid_rowconfigure(5, weight=0, minsize=40, pad=0)
        root.grid_rowconfigure(6, weight=0, minsize=40, pad=0)
        root.grid_rowconfigure(7, weight=1, minsize=40, pad=0)
        root.grid_rowconfigure(8, weight=0, minsize=65, pad=0)
        root.grid_columnconfigure(1, weight=0, minsize=152, pad=0)
        root.grid_columnconfigure(2, weight=0, minsize=152, pad=0)
        root.grid_columnconfigure(3, weight=0, minsize=106, pad=0)
        root.grid_columnconfigure(4, weight=0, minsize=99, pad=0)


class CustomMain(Main):
    mode=""
    print("Login Successful")
    messagebox.showinfo("Success", u"Login Successful..!!!\u263A\u263A\u263A")

    def _button_1_command(self, *args):
        print("Submit Button Pressed.")
        rando = ''.join([random.choice(string.ascii_letters
                                        + string.digits) for n in range(10)])
        if via == "1":
            mode="Paytm"
        elif via == "2":
            mode = "UPI"
        elif via == "3":
            mode = "Pay By Cash"
        try:
            if self.name.get()=="":
                print("Enter all details before proceeding.")
                messagebox.showerror("Error","Enter all the details before proceeding...!!")
            else:
                print("Value = "+ mode)
                messagebox.showinfo("Thank You For Booking.",
                            "**********  Transaction Id = " + str(rando).upper() +"  **********"+ "\n\nName = " + str(self.name.get()) + "\nFrom = " + str(
                                self.fromspinner.get()) +
                            "\nDestination = " + str(self.destinationspinner.get()) + "\nDate = " + str(
                                self._entry_1.get()) +
                            "\nFare = " + str(self.fare["text"]) + "\nPayment Mode = " + mode + "\n\n***************************************************" + u"\n\n\n\tWe wish to see you again....!!!\u263A\u263A\u263A")
        except:
            messagebox.showerror("Error", "Something went wrong..!")

        pass

def main():
    root = Tk()
    demo = CustomMain(root)
    root.title('main')
    root.mainloop()

if __name__ == '__main__': main()
