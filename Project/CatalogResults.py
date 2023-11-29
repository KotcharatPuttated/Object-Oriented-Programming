import os
import imp
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import CatalogResults_support
import search_support
import Resevation_support
import ProfileCus_support

userpath = os.path.expanduser("~")
targetpath = userpath+"/Downloads/OOP(1)/OOP/GUi/Login/image/"

class Toplevel1:     
    def open_Resevation(self):
        self.top.destroy()
        Resevation_support.main()
        
    def open_search(self):
        self.top.destroy()
        search_support.main()
        
    def open_profile(self):
        self.top.destroy()
        ProfileCus_support.main()
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffc61a'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffc61a' # X11 color: 'gray85'
        _ana1color = '#ffc61a' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
            self.style.configure('.',background=_bgcolor)
            self.style.configure('.',foreground=_fgcolor)
            self.style.configure('.',font="TkDefaultFont")
            self.style.map('.',background=
                [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("800x700+447+53")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("JONG NONG")
        top.configure(background="#fff4ea")
        top.configure(highlightbackground="#ffc61a")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.038, rely=0.2, relheight=0.773, relwidth=0.9)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffc61a")
        self.Frame1.configure(highlightbackground="#ffc61a")
        self.Frame1.configure(highlightcolor="black")

        self.TButton1 = ttk.Button(self.Frame1)
        self.TButton1.place(relx=0.068, rely=0.037, height=200, width=180)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Tbutton''')
        photo_location = targetpath+"cat01.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.TButton1.configure(image=_img0)
        self.TButton1.configure(compound='left')
        self.TButton1.configure(command=self.open_Resevation)

        self.TButton2 = ttk.Button(self.Frame1)
        self.TButton2.place(relx=0.068, rely=0.518, height=200, width=180)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Tbutton''')
        photo_location = targetpath+"cat3.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.TButton2.configure(image=_img1)
        self.TButton2.configure(compound='left')
        self.TButton2.configure(command=self.open_Resevation)

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.095, rely=0.425, height=31, width=150)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ffc61a")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Comic Sans MS} -size 12")
        self.Label1.configure(foreground="#440a00")
        self.Label1.configure(highlightbackground="#ffc61a")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Price__________฿''')

        self.TButton3 = ttk.Button(self.Frame1)
        self.TButton3.place(relx=0.689, rely=0.037, height=200, width=180)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Tbutton''')
        photo_location = targetpath+"cat3.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.TButton3.configure(image=_img2)
        self.TButton3.configure(compound='left')
        self.TButton3.configure(command=self.open_Resevation)

        self.TButton4 = ttk.Button(self.Frame1)
        self.TButton4.place(relx=0.378, rely=0.037, height=200, width=180)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Tbutton''')
        photo_location = targetpath+"cat2.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.TButton4.configure(image=_img3)
        self.TButton4.configure(compound='left')
        self.TButton4.configure(command=self.open_Resevation)

        self.TButton5 = ttk.Button(self.Frame1)
        self.TButton5.place(relx=0.378, rely=0.518, height=200, width=180)
        self.TButton5.configure(takefocus="")
        self.TButton5.configure(text='''Tbutton''')
        photo_location = targetpath+"cat01.png"
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.TButton5.configure(image=_img4)
        self.TButton5.configure(compound='left')
        self.TButton5.configure(command=self.open_Resevation)

        self.TButton6 = ttk.Button(self.Frame1)
        self.TButton6.place(relx=0.703, rely=0.518, height=200, width=180)
        self.TButton6.configure(takefocus="")
        self.TButton6.configure(text='''Tbutton''')
        photo_location = targetpath+"cat2.png"
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.TButton6.configure(image=_img5)
        self.TButton6.configure(compound='left')
        self.TButton6.configure(command=self.open_Resevation)

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.405, rely=0.425, height=31, width=150)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ffc61a")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Comic Sans MS} -size 12")
        self.Label2.configure(foreground="#440a00")
        self.Label2.configure(highlightbackground="#ffc61a")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Price__________฿''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.73, rely=0.425, height=31, width=150)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#ffc61a")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Comic Sans MS} -size 12")
        self.Label3.configure(foreground="#440a00")
        self.Label3.configure(highlightbackground="#ffc61a")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Price__________฿''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.095, rely=0.906, height=31, width=150)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#ffc61a")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Comic Sans MS} -size 12")
        self.Label4.configure(foreground="#440a00")
        self.Label4.configure(highlightbackground="#ffc61a")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Price__________฿''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.419, rely=0.906, height=31, width=149)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#ffc61a")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5.configure(foreground="#440a00")
        self.Label5.configure(highlightbackground="#ffc61a")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Price__________฿''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.743, rely=0.906, height=31, width=150)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#ffc61a")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Comic Sans MS} -size 12")
        self.Label6.configure(foreground="#440a00")
        self.Label6.configure(highlightbackground="#ffc61a")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Price__________฿''')

        self.Label7 = tk.Label(self.top)
        self.Label7.place(relx=0.388, rely=0.02, height=61, width=208)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#fff4ea")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Arial Rounded MT Bold} -size 36 -weight bold")
        self.Label7.configure(foreground="#440a00")
        self.Label7.configure(highlightbackground="#ffc61a")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Catalog''')

        self.Label8 = tk.Label(self.top)
        self.Label8.place(relx=0.36, rely=0.11, height=31, width=280)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#fff4ea")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Comic Sans MS} -size 20")
        self.Label8.configure(foreground="white")
        self.Label8.configure(highlightbackground="#ffc61a")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''" Search Results "''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        
        

        
        
        
 
        self.Button07 = tk.Button(self.top)
        self.Button07.place(relx=0.03, rely=0.128, height=50, width=150)
        self.Button07.configure(activebackground="#fff4ea")
        self.Button07.configure(activeforeground="#fff4ea")
        self.Button07.configure(background="#fff4ea")
        self.Button07.configure(compound='left')
        self.Button07.configure(disabledforeground="#fff4ea")
        self.Button07.configure(foreground="#fff4ea")
        self.Button07.configure(highlightbackground="#fff4ea")
        self.Button07.configure(highlightcolor="#fff4ea")
        self.Button07.configure(font="-family {Comic Sans MS} -size 18 -weight bold")
        self.Button07.configure(foreground="#372a28")
        self.Button07.configure(text=''' Profile''')
        photo_location = targetpath+"profile50.png"
        global _img002
        _img002 = tk.PhotoImage(file=photo_location)
        self.Button07.configure(image=_img002)
        self.Button07.configure(pady="0")
        self.Button07.configure(relief="flat")
        self.Button07.configure(command=self.open_profile)
        
        self.Button7 = tk.Button(self.top)
        self.Button7.place(relx=0.25, rely=0.128, height=50, width=150)
        self.Button7.configure(activebackground="#fff4ea")
        self.Button7.configure(activeforeground="#fff4ea")
        self.Button7.configure(background="#fff4ea")
        self.Button7.configure(compound='left')
        self.Button7.configure(disabledforeground="#fff4ea")
        self.Button7.configure(foreground="#fff4ea")
        self.Button7.configure(highlightbackground="#fff4ea")
        self.Button7.configure(highlightcolor="#fff4ea")
        self.Button7.configure(font="-family {Comic Sans MS} -size 18 -weight bold")
        self.Button7.configure(foreground="#372a28")
        self.Button7.configure(text='''Search''')
        photo_location = targetpath+"search50x50.png"
        global _img003
        _img003 = tk.PhotoImage(file=photo_location)
        self.Button7.configure(image=_img003)
        self.Button7.configure(pady="0")
        self.Button7.configure(relief="flat")
        self.Button7.configure(command=self.open_search)
        
        
        
        

def start_up():
    CatalogResults_support.main()

if __name__ == '__main__':
    CatalogResults_support.main()




