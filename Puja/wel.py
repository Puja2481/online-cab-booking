

from tkinter import *
from wel_ui import Wel
from tkinter import messagebox
import tkinter
# BEGIN USER CODE global

# END USER CODE global

class CustomWel(Wel):
    pass

    # BEGIN CALLBACK CODE
    # about_command --
    #
    # Callback to handle about widget option -command
    def about_command(self, *args):
        import aboutus
        self.newwindow = tkinter.Toplevel()
        self.demo = aboutus.CustomAboutus(self.newwindow)
        pass

    # exit_command --
    #
    # Callback to handle exit widget option -command
    def exit_command(self, *args):
        print("Exit Button Pressed.")
        msg = messagebox.askyesno("Exit", "Are you sure you want to exit ?", icon='warning')
        if msg:
            print("Welcome Window Closed.")
            quit(0)
        pass

    # login_command --
    #
    # Callback to handle login widget option -command
    def login_command(self, *args):
        print("Login Button Pressed.")
        import Loginuser
        self.newwindow = tkinter.Toplevel()
        self.demo = Loginuser.CustomLogin(self.newwindow)
        pass

    # new_user_command --
    #
    # Callback to handle new_user widget option -command
    def new_user_command(self, *args):
        print("New User Button Pressed.")
        import newuser1
        self.newwindow = tkinter.Toplevel()
        self.demo = newuser1.CustomNewuser(self.newwindow)
        pass

    # END CALLBACK CODE

    # BEGIN USER CODE class

    # END USER CODE class

def main():
    root = Tk()
    demo = CustomWel(root)
    root.title('Welcome')
    root.mainloop()

if __name__ == '__main__': main()
