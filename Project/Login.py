import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Login_support
import Register_support
import search_support

import os
userpath = os.path.expanduser("~")
targetpath = userpath+"/Downloads/OOP(1)/OOP/GUi/Login/image/"


class Toplevel1:
    
    def open_register(self):
        self.top.destroy()
        Register_support.main()
    
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

        top.geometry("800x700+443+8")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("JONG NONG")
        top.configure(background="#fff4ea")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.263, rely=0.029, height=61, width=417)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#fff4ea")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial Rounded MT Bold} -size 48")
        self.Label1.configure(foreground="#440a00")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Welcome to''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.325, rely=0.114, height=51, width=315)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        
        self.Label2.configure(background="#fff4ea")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Comic Sans MS} -size 18 ")
        self.Label2.configure(foreground="#440a00")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''JONG NONG (Cat Shop)''')

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.413, rely=0.243, relheight=0.58, relwidth=0.531)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffc61a")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Entry2 = tk.Entry(self.Frame1)
        self.Entry2.place(relx=0.165, rely=0.246, relheight=0.099, relwidth=0.706)
        self.Entry2.configure(background="#372a28")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="white")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="white")

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.165, rely=0.468, height=40, relwidth=0.706)
        self.Entry1.configure(background="#372a28")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="white")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")
        

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.65, rely=0.257, height=51, width=87)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#ffc61a")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Comic Sans MS} -size 24 -weight bold")
        self.Label3.configure(foreground="#440a00")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Login''')
        

        self.Label4 = tk.Label(self.top)
        self.Label4.place(relx=0.5, rely=0.329, height=31, width=115)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#ffc61a")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Comic Sans MS} -size 16")
        self.Label4.configure(foreground="#440a00")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Usrename :''')

        self.Label5 = tk.Label(self.top)
        self.Label5.place(relx=0.498, rely=0.469, height=31, width=96)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#ffc61a")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Comic Sans MS} -size 16")
        self.Label5.configure(foreground="#440a00")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Password :''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.725, rely=0.629, height=36, width=105)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#372a28")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Sign In''')
        self.Button1.configure(command=self.open_search)


        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.55, rely=0.629, height=36, width=105)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#372a28")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Register''')
        self.Button2.configure(command=self.open_register)

        self.Label6 = tk.Label(self.top)
        self.Label6.place(relx=0.75, rely=0.0, height=130, width=130)
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#fff4ea")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        photo_location = targetpath+"cat001.png"
        global _img06
        _img06 = tk.PhotoImage(file=photo_location)
        self.Label6.configure(image=_img06)
        self.Label6.configure(text='''Label''')

        self.Label06 = tk.Label(self.top)
        self.Label06.place(relx=0.075, rely=0.357, height=220, width=220)
        self.Label06.configure(anchor='w')
        self.Label06.configure(background="#fff4ea")
        self.Label06.configure(compound='left')
        self.Label06.configure(disabledforeground="#a3a3a3")
        self.Label06.configure(foreground="#000000")
        photo_location = targetpath+"Logo.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label06.configure(image=_img0)
        self.Label06.configure(text='''Label''')

def start_up():
    Login_support.main()

if __name__ == '__main__':
    Login_support.main()




