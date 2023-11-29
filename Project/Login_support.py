import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Login

def main(*args,close=False):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global top1, _w1
    top1 = root
    _w1 = Login.Toplevel1(top1)
    root.mainloop()

if __name__ == '__main__':
    Login.start_up()




