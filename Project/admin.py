import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import admin_support
import search_support
import Add_support
import ManageAccount_support
import Login_support
userpath = os.path.expanduser("~")
targetpath = userpath+"/Downloads/OOP(1)/OOP/GUi/Login/image/"

class Toplevel1:
    
    def open_login(self):
        self.top.destroy()
        Login_support.main()
    
    def open_add(self):
        self.top.destroy()
        Add_support.main()
    
    def open_manageCustomer(self):
        self.top.destroy()
        ManageAccount_support.main()
        
    def open_search(self):
        self.top.destroy()
        search_support.main()
        
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("800x700+380+39")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("JONG NONG")
        top.configure(background="#fff4ea")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top
        
        self.Search = tk.Button(self.top)
        self.Search.place(relx=0.913, rely=0.029, height=50, width=50)
        self.Search.configure(background="#fff4ea")
        self.Search.configure(compound='left')
        self.Search.configure(foreground="#fff4ea")
        self.Search.configure(font="-family {Comic Sans MS} -size 18 -weight bold")
        self.Search.configure(foreground="#372a28")
        self.Search.configure(text='''''')
        photo_location = targetpath+"search50x50.png"
        global _img003
        _img003 = tk.PhotoImage(file=photo_location)
        self.Search.configure(image=_img003)
        self.Search.configure(pady="0")
        self.Search.configure(relief="flat")
        self.Search.configure(command=self.open_search)
        
        
        
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.525, rely=0.129, height=120, width=131)
        self.Label1.configure(activebackground="#fff4ea")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#fff4ea")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#372a28")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = targetpath+"admimicon120.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.5, rely=0.0, height=72, width=146)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#fff4ea")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial Rounded MT Bold} -size 30")
        self.Label2.configure(foreground="#372a28")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Admin''')


        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.0, rely=-0.029, relheight=1.05, relwidth=0.181)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffc61a")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.06, rely=0.04, height=110, width=111)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#ffc61a")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        photo_location = targetpath+"logo110x110.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label3.configure(image=_img1)
        self.Label3.configure(text='''Label''')
        
        self.Button2_1 = tk.Button(self.Frame2)
        self.Button2_1.place(relx=0.021, rely=0.9, height=56, width=136)
        self.Button2_1.configure(activebackground="#ececec")
        self.Button2_1.configure(activeforeground="#000000")
        self.Button2_1.configure(background="#ffc61a")
        self.Button2_1.configure(compound='left')
        self.Button2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1.configure(font="-family {Comic Sans MS} -size 16 -weight bold")
        self.Button2_1.configure(foreground="#000000")
        self.Button2_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1.configure(highlightcolor="black")
        photo_location = targetpath+"iconlogout50.png"
        global _img51
        _img51 = tk.PhotoImage(file=photo_location)
        self.Button2_1.configure(image=_img51)
        self.Button2_1.configure(pady="0")
        self.Button2_1.configure(relief="flat")
        self.Button2_1.configure(text='''Logout''')
        self.Button2_1.configure(command=self.open_login)


        self.TSeparator2 = ttk.Separator(self.top)
        self.TSeparator2.place(relx=0.463, rely=0.086,  relwidth=0.25)

        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.188, rely=0.329,  relwidth=0.826)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.225, rely=0.343, relheight=0.107
                , relwidth=0.719)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffc61a")

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.034, rely=0.267, height=32, width=248)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#ffc61a")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Comic Sans MS} -size 14")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Name :_______________''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.504, rely=0.267, height=32, width=267)
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#ffc61a")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Comic Sans MS} -size 14")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Admit ID :______________''')      

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.225, rely=0.486, relheight=0.364
                , relwidth=0.719)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffc61a")

        self.Button5 = tk.Button(self.Frame2)
        self.Button5.place(relx=0.546, rely=0.65, height=40, width=180)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#372a28")
        self.Button5.configure(compound='left')
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Comic Sans MS} -size 14")
        self.Button5.configure(foreground="#ffffff")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Manage Product''')
        self.Button5.configure(command=self.open_add)

        self.Button5_1 = tk.Button(self.Frame2)
        self.Button5_1.place(relx=0.212, rely=0.65, height=40, width=180)
        self.Button5_1.configure(activebackground="#ececec")
        self.Button5_1.configure(activeforeground="#000000")
        self.Button5_1.configure(background="#372a28")
        self.Button5_1.configure(compound='left')
        self.Button5_1.configure(disabledforeground="#a3a3a3")
        self.Button5_1.configure(font="-family {Comic Sans MS} -size 14")
        self.Button5_1.configure(foreground="#d9d9d9")
        self.Button5_1.configure(highlightbackground="#d9d9d9")
        self.Button5_1.configure(highlightcolor="black")
        self.Button5_1.configure(pady="0")
        self.Button5_1.configure(text='''Manage Customer''')
        self.Button5_1.configure(command=self.open_manageCustomer)
        


        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.4, rely=0.039, height=150, width=150)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#ffc61a")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        photo_location = targetpath+"map150.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Label4.configure(image=_img3)

def start_up():
    admin_support.main()

if __name__ == '__main__':
    admin_support.main()




