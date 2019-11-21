
from tkinter import *
from aboutus_ui import Aboutus
class CustomAboutus(Aboutus):
    pass
    def close_command(self):
        print("Close Buttton pressed.")
        print("About Us Window Closed.")
        quit(0)
        pass
def main():
    try: userinit()
    except NameError: pass
    root = Tk()
    demo = CustomAboutus(root)
    root.title('aboutus')
    try: run()
    except NameError: pass
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

if __name__ == '__main__': main()
