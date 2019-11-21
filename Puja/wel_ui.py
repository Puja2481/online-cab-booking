
import tkinter
class Wel(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('Capture4.GIF', file = 'Capture4.GIF'))
        self._images.append(tkinter.PhotoImage('Capture7.GIF', file = 'Capture7.GIF'))


        # Widget Initialization
        self._label_4 = tkinter.Label(root,
            activebackground = "#000000",
            background = "#000000",
            image = "Capture7.GIF",
            text = "_label_4",
        )
        self._label_6 = tkinter.Label(root,
            image = "Capture4.GIF",
            text = "_label_6",
        )
        self.about = tkinter.Button(root,
            activebackground = "#cccccc",
            background = "#cccccc",
            borderwidth = 5,
            font = "{MS Sans Serif} 16 bold",
            text = "About",
        )
        self.login = tkinter.Button(root,
            activebackground = "#999999",
            background = "#999999",
            borderwidth = 5,
            font = "{MS Sans Serif} 14 bold",
            text = "Login",
        )
        self.new_user = tkinter.Button(root,
            activebackground = "#cccccc",
            background = "#cccccc",
            borderwidth = 5,
            font = "{MS Sans Serif} 14 bold",
            text = "New User",
        )
        self.exit = tkinter.Button(root,
            borderwidth = 5,
            font = "{MS Sans Serif} 14 bold",
            text = "Exit",
        )

        # widget commands

        self.about.configure(
            command = self.about_command
        )
        self.login.configure(
            command = self.login_command
        )
        self.new_user.configure(
            command = self.new_user_command
        )
        self.exit.configure(
            command = self.exit_command
        )


        # Geometry Management
        self._label_4.grid(
            in_    = root,
            column = 1,
            row    = 2,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_6.grid(
            in_    = root,
            column = 1,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = ""
        )
        self.about.grid(
            in_    = root,
            column = 1,
            row    = 3,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.login.grid(
            in_    = root,
            column = 1,
            row    = 4,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.new_user.grid(
            in_    = root,
            column = 1,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.exit.grid(
            in_    = root,
            column = 1,
            row    = 6,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )


        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 155, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(4, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(5, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(6, weight = 0, minsize = 40, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 301, pad = 0)


