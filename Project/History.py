import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import History_support
import ProfileCus_support
import Login_support
import search_support

import os
userpath = os.path.expanduser("~")
targetpath = userpath+"/Downloads/OOP(1)/OOP/GUi/Login/image/"

class Toplevel1:
    
    def open_search(self):
        self.top.destroy()
        search_support.main()
    
    def open_profile(self):
        self.top.destroy()
        ProfileCus_support.main()
        
    def open_login(self):
        self.top.destroy()
        Login_support.main()
        
        
        
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

        top.geometry("800x700+324+38")
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
        self.Label1.place(relx=0.5, rely=0.114, height=150, width=150)
        self.Label1.configure(activebackground="#fff4ea")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#fff4ea")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#372a28")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        photo_location = targetpath+"iconuser150.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.513, rely=0.0, height=72, width=146)
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
        self.Label2.configure(text='''Profile''')

        self.TSeparator2 = ttk.Separator(self.top)
        self.TSeparator2.place(relx=0.463, rely=0.086,  relwidth=0.25)

        self.TSeparator3 = ttk.Separator(self.top)
        self.TSeparator3.place(relx=0.175, rely=0.343,  relwidth=0.826)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.213, rely=0.529, relheight=0.064
                , relwidth=0.744)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#c0c0c0")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.042, rely=0.222, height=29, width=103)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#c0c0c0")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''C64015024''')

        self.Label5_1 = tk.Label(self.Frame1)
        self.Label5_1.place(relx=0.343, rely=0.222, height=29, width=73)
        self.Label5_1.configure(activebackground="#f9f9f9")
        self.Label5_1.configure(activeforeground="black")
        self.Label5_1.configure(anchor='w')
        self.Label5_1.configure(background="#c0c0c0")
        self.Label5_1.configure(compound='left')
        self.Label5_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5_1.configure(foreground="#000000")
        self.Label5_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1.configure(highlightcolor="black")
        self.Label5_1.configure(text='''35000''')

        self.Label5_1_1 = tk.Label(self.Frame1)
        self.Label5_1_1.place(relx=0.543, rely=0.222, height=29, width=113)
        self.Label5_1_1.configure(activebackground="#f9f9f9")
        self.Label5_1_1.configure(activeforeground="black")
        self.Label5_1_1.configure(anchor='w')
        self.Label5_1_1.configure(background="#c0c0c0")
        self.Label5_1_1.configure(compound='left')
        self.Label5_1_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1_1.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5_1_1.configure(foreground="#000000")
        self.Label5_1_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1_1.configure(highlightcolor="black")
        self.Label5_1_1.configure(text='''12/05/2564''')

        self.Label5_1_1_1 = tk.Label(self.Frame1)
        self.Label5_1_1_1.place(relx=0.807, rely=0.156, height=29, width=83)
        self.Label5_1_1_1.configure(activebackground="#f9f9f9")
        self.Label5_1_1_1.configure(activeforeground="black")
        self.Label5_1_1_1.configure(anchor='w')
        self.Label5_1_1_1.configure(background="#c0c0c0")
        self.Label5_1_1_1.configure(compound='left')
        self.Label5_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label5_1_1_1.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5_1_1_1.configure(foreground="#008000")
        self.Label5_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label5_1_1_1.configure(highlightcolor="black")
        self.Label5_1_1_1.configure(text='''Succeed''')

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.0, rely=-0.029, relheight=1.05, relwidth=0.181)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffc61a")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Button2_1 = tk.Button(self.Frame2)
        self.Button2_1.place(relx=0.021, rely=0.893, height=56, width=136)
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
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Button2_1.configure(image=_img1)
        self.Button2_1.configure(pady="0")
        self.Button2_1.configure(relief="flat")
        self.Button2_1.configure(text='''Logout''')
        self.Button2_1.configure(command=self.open_login)


        self.Label3_1 = tk.Label(self.Frame2)
        self.Label3_1.place(relx=0.131, rely=0.054, height=110, width=111)
        self.Label3_1.configure(activebackground="#ffc61a")
        self.Label3_1.configure(activeforeground="black")
        self.Label3_1.configure(anchor='w')
        self.Label3_1.configure(background="#ffc61a")
        self.Label3_1.configure(compound='left')
        self.Label3_1.configure(disabledforeground="#a3a3a3")
        self.Label3_1.configure(foreground="#000000")
        self.Label3_1.configure(highlightbackground="#d9d9d9")
        self.Label3_1.configure(highlightcolor="black")
        photo_location = targetpath+"logo110x110.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Label3_1.configure(image=_img2)
        self.Label3_1.configure(text='''Label''')

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.069, rely=0.259, height=40, width=120)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#372a28")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Comic Sans MS} -size 16 -weight bold")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''My Profile''')
        self.Button1.configure(command=self.open_profile)

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.288, rely=0.369, height=44, width=303)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#fff4ea")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Comic Sans MS} -size 20 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Reservation History''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.213, rely=0.36, height=50, width=60)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#fff4ea")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        photo_location = targetpath+"iconhistory.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Label4.configure(image=_img3)

        self.Frame3 = tk.Frame(self.top)
        self.Frame3.place(relx=0.213, rely=0.443, relheight=0.079
                , relwidth=0.744)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#ffc61a")

        self.Label6_1 = tk.Label(self.Frame3)
        self.Label6_1.place(relx=0.035, rely=0.091, height=32, width=76)
        self.Label6_1.configure(activebackground="#f9f9f9")
        self.Label6_1.configure(activeforeground="black")
        self.Label6_1.configure(anchor='w')
        self.Label6_1.configure(background="#ffc61a")
        self.Label6_1.configure(compound='left')
        self.Label6_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Label6_1.configure(foreground="#000000")
        self.Label6_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1.configure(highlightcolor="black")
        self.Label6_1.configure(text='''Cat ID''')

        self.Label6_1_1 = tk.Label(self.Frame3)
        self.Label6_1_1.place(relx=0.35, rely=0.127, height=32, width=76)
        self.Label6_1_1.configure(activebackground="#f9f9f9")
        self.Label6_1_1.configure(activeforeground="black")
        self.Label6_1_1.configure(anchor='w')
        self.Label6_1_1.configure(background="#ffc61a")
        self.Label6_1_1.configure(compound='left')
        self.Label6_1_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1_1.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Label6_1_1.configure(foreground="#000000")
        self.Label6_1_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1_1.configure(highlightcolor="black")
        self.Label6_1_1.configure(text='''Price''')

        self.Label6_1_1_1 = tk.Label(self.Frame3)
        self.Label6_1_1_1.place(relx=0.585, rely=0.127, height=32, width=76)
        self.Label6_1_1_1.configure(activebackground="#f9f9f9")
        self.Label6_1_1_1.configure(activeforeground="black")
        self.Label6_1_1_1.configure(anchor='w')
        self.Label6_1_1_1.configure(background="#ffc61a")
        self.Label6_1_1_1.configure(compound='left')
        self.Label6_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1_1_1.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Label6_1_1_1.configure(foreground="#000000")
        self.Label6_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1_1_1.configure(highlightcolor="black")
        self.Label6_1_1_1.configure(text='''Date''')

        self.Label6_1_1_1_1 = tk.Label(self.Frame3)
        self.Label6_1_1_1_1.place(relx=0.803, rely=0.164, height=32, width=76)
        self.Label6_1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label6_1_1_1_1.configure(activeforeground="black")
        self.Label6_1_1_1_1.configure(anchor='w')
        self.Label6_1_1_1_1.configure(background="#ffc61a")
        self.Label6_1_1_1_1.configure(compound='left')
        self.Label6_1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1_1_1_1.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Label6_1_1_1_1.configure(foreground="#000000")
        self.Label6_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1_1_1_1.configure(highlightcolor="black")
        self.Label6_1_1_1_1.configure(text='''Status''')

        self.Frame1_1 = tk.Frame(self.top)
        self.Frame1_1.place(relx=0.213, rely=0.6, relheight=0.064
                , relwidth=0.744)
        self.Frame1_1.configure(relief='groove')
        self.Frame1_1.configure(borderwidth="2")
        self.Frame1_1.configure(relief="groove")
        self.Frame1_1.configure(background="#c0c0c0")
        self.Frame1_1.configure(highlightbackground="#d9d9d9")
        self.Frame1_1.configure(highlightcolor="black")

        self.Label5_2 = tk.Label(self.Frame1_1)
        self.Label5_2.place(relx=0.05, rely=0.222, height=29, width=103)
        self.Label5_2.configure(activebackground="#f9f9f9")
        self.Label5_2.configure(activeforeground="black")
        self.Label5_2.configure(anchor='w')
        self.Label5_2.configure(background="#c0c0c0")
        self.Label5_2.configure(compound='left')
        self.Label5_2.configure(disabledforeground="#a3a3a3")
        self.Label5_2.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5_2.configure(foreground="#000000")
        self.Label5_2.configure(highlightbackground="#d9d9d9")
        self.Label5_2.configure(highlightcolor="black")
        self.Label5_2.configure(text='''C65401521''')

        self.Label5_1_2 = tk.Label(self.Frame1_1)
        self.Label5_1_2.place(relx=0.343, rely=0.222, height=29, width=73)
        self.Label5_1_2.configure(activebackground="#f9f9f9")
        self.Label5_1_2.configure(activeforeground="black")
        self.Label5_1_2.configure(anchor='w')
        self.Label5_1_2.configure(background="#c0c0c0")
        self.Label5_1_2.configure(compound='left')
        self.Label5_1_2.configure(disabledforeground="#a3a3a3")
        self.Label5_1_2.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5_1_2.configure(foreground="#000000")
        self.Label5_1_2.configure(highlightbackground="#d9d9d9")
        self.Label5_1_2.configure(highlightcolor="black")
        self.Label5_1_2.configure(text='''40251''')

        self.Label5_1_1_2 = tk.Label(self.Frame1_1)
        self.Label5_1_1_2.place(relx=0.543, rely=0.222, height=29, width=113)
        self.Label5_1_1_2.configure(activebackground="#f9f9f9")
        self.Label5_1_1_2.configure(activeforeground="black")
        self.Label5_1_1_2.configure(anchor='w')
        self.Label5_1_1_2.configure(background="#c0c0c0")
        self.Label5_1_1_2.configure(compound='left')
        self.Label5_1_1_2.configure(disabledforeground="#a3a3a3")
        self.Label5_1_1_2.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5_1_1_2.configure(foreground="#000000")
        self.Label5_1_1_2.configure(highlightbackground="#d9d9d9")
        self.Label5_1_1_2.configure(highlightcolor="black")
        self.Label5_1_1_2.configure(text='''08/06/2564''')

        self.Cancel = tk.Button(self.Frame1_1)
        self.Cancel.place(relx=0.798, rely=0.156, height=30, width=80)

        self.Cancel.configure(background="#372a28")
        self.Cancel.configure(compound='left')

        self.Cancel.configure(font="-family {Comic Sans MS} -size 12")
        self.Cancel.configure(foreground="white")
        self.Cancel.configure(highlightbackground="#d9d9d9")
        self.Cancel.configure(highlightcolor="black")
        self.Cancel.configure(pady="0")
        self.Cancel.configure(text='''Cancel''')


def start_up():
    History_support.main()

if __name__ == '__main__':
    History_support.main()




