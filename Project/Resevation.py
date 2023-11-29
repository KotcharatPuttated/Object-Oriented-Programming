import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Resevation_support
import CatalogResults_support

import os
userpath = os.path.expanduser("~")
targetpath = userpath+"/Downloads/OOP(1)/OOP/GUi/Login/image/"

class Toplevel1:
    def open_catalog(self):
        self.top.destroy()
        CatalogResults_support.main()
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffc61a'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffc61a' # X11 color: 'gray85'
        _ana1color = '#ffc61a' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("800x700+448+17")
        top.minsize(800, 700)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("JONG NONG")
        top.configure(background="#fff4ea")
        top.configure(highlightbackground="#ffc61a")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.363, rely=0.014, height=51, width=236)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#fff4ea")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial Rounded MT Bold} -size 30")
        self.Label1.configure(foreground="#372a28")
        self.Label1.configure(highlightbackground="#ffc61a")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Resevation''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.413, rely=0.1, height=150, width=152)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#fff4ea")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#372a28")
        self.Label2.configure(highlightbackground="#ffc61a")
        self.Label2.configure(highlightcolor="black")
        photo_location = targetpath+"cat1.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label2.configure(image=_img0)
        self.Label2.configure(text='''Label''')

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.05, rely=0.371, relheight=0.179, relwidth=0.894)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffc61a")
        self.Frame1.configure(highlightbackground="#ffc61a")
        self.Frame1.configure(highlightcolor="black")

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.014, rely=0.08, height=21, width=234)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#ffc61a")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Comic Sans MS} -size 14")
        self.Label4.configure(foreground="#372a28")
        self.Label4.configure(highlightbackground="#ffc61a")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Cat ID :____________________''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.392, rely=0.08, height=21, width=164)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#ffc61a")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Comic Sans MS} -size 14")
        self.Label5.configure(foreground="#372a28")
        self.Label5.configure(highlightbackground="#ffc61a")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Gender :__________''')

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.671, rely=0.08, height=21, width=194)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#ffc61a")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font="-family {Comic Sans MS} -size 14")
        self.Label6.configure(foreground="#372a28")
        self.Label6.configure(highlightbackground="#ffc61a")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Color : _______________''')

        self.Label7 = tk.Label(self.Frame1)
        self.Label7.place(relx=0.014, rely=0.56, height=30, width=214)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#ffc61a")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Comic Sans MS} -size 14")
        self.Label7.configure(foreground="#372a28")
        self.Label7.configure(highlightbackground="#ffc61a")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Species : _______________''')

        self.Label8 = tk.Label(self.Frame1)
        self.Label8.place(relx=0.322, rely=0.56, height=31, width=250)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#ffc61a")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Comic Sans MS} -size 14")
        self.Label8.configure(foreground="#372a28")
        self.Label8.configure(highlightbackground="#ffc61a")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Deposit : ________Bath''')

        self.Label3 = tk.Label(self.top)
        self.Label3.place(relx=0.05, rely=0.314, height=31, width=210)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#fff4ea")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Comic Sans MS} -size 16")
        self.Label3.configure(foreground="light yellow")
        self.Label3.configure(highlightbackground="#ffc61a")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Product Information''')

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.05, rely=0.614, relheight=0.18, relwidth=0.894)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffc61a")
        self.Frame2.configure(highlightbackground="#ffc61a")
        self.Frame2.configure(highlightcolor="black")

        self.Label9 = tk.Label(self.Frame2)
        self.Label9.place(relx=0.434, rely=0.079, height=31, width=284)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#ffc61a")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(font="-family {Comic Sans MS} -size 14")
        self.Label9.configure(foreground="#372a28")
        self.Label9.configure(highlightbackground="#ffc61a")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Member ID :______________________''')

        self.Label10 = tk.Label(self.Frame2)
        self.Label10.place(relx=0.028, rely=0.079, height=31, width=234)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#ffc61a")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Comic Sans MS} -size 14")
        self.Label10.configure(foreground="#372a28")
        self.Label10.configure(highlightbackground="#ffc61a")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Name :____________________''')

        self.Label11 = tk.Label(self.Frame2)
        self.Label11.place(relx=0.028, rely=0.476, height=31, width=304)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#ffc61a")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Comic Sans MS} -size 14")
        self.Label11.configure(foreground="#372a28")
        self.Label11.configure(highlightbackground="#ffc61a")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Phone Number :_________________''')

        self.Label12 = tk.Label(self.Frame2)
        self.Label12.place(relx=0.462, rely=0.714, height=21, width=105)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#ffc61a")
        self.Label12.configure(compound='left')
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font="-family {Comic Sans MS} -size 13")
        self.Label12.configure(foreground="#372a28")
        self.Label12.configure(highlightbackground="#ffc61a")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''Pay time :''')

        self.Label13 = tk.Label(self.Frame2)
        self.Label13.place(relx=0.727, rely=0.635, height=31, width=93)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#ffc61a")
        self.Label13.configure(compound='left')
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font="-family {Comic Sans MS} -size 13")
        self.Label13.configure(foreground="#372a28")
        self.Label13.configure(highlightbackground="#ffc61a")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(text='''Pay date :''')

        self.Entry1 = tk.Entry(self.Frame2)
        self.Entry1.place(relx=0.587, rely=0.714, height=20, relwidth=0.112)
        self.Entry1.configure(background="#372a28")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="white")
        self.Entry1.configure(highlightbackground="#ffc61a")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="#372a28")

        self.Label14 = tk.Label(self.Frame2)
        self.Label14.place(relx=0.601, rely=0.476, height=21, width=63)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(anchor='w')
        self.Label14.configure(background="#ffc61a")
        self.Label14.configure(compound='left')
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(font="-family {Comic Sans MS} -size 10")
        self.Label14.configure(foreground="#372a28")
        self.Label14.configure(highlightbackground="#ffc61a")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''HH : MM''')

        self.Entry2 = tk.Entry(self.Frame2)
        self.Entry2.place(relx=0.853, rely=0.714, height=20, relwidth=0.126)
        self.Entry2.configure(background="#372a28")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="white")
        self.Entry2.configure(highlightbackground="#ffc61a")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="blue")
        self.Entry2.configure(selectforeground="#372a28")

        self.Label15 = tk.Label(self.Frame2)
        self.Label15.place(relx=0.867, rely=0.476, height=21, width=74)
        self.Label15.configure(activebackground="#f9f9f9")
        self.Label15.configure(activeforeground="black")
        self.Label15.configure(anchor='w')
        self.Label15.configure(background="#ffc61a")
        self.Label15.configure(compound='left')
        self.Label15.configure(disabledforeground="#a3a3a3")
        self.Label15.configure(font="-family {Comic Sans MS} -size 10")
        self.Label15.configure(foreground="#372a28")
        self.Label15.configure(highlightbackground="#ffc61a")
        self.Label15.configure(highlightcolor="black")
        self.Label15.configure(text='''DD/MM/YY''')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.363, rely=0.82, height=54, width=217)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#372a28")
        self.Button1.configure(background="#372a28")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Comic Sans MS} -size 16")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#ffc61a")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Reservation Now !''')
        
        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.73, rely=0.82, height=50, width=50)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(background="#fff4ea")
        self.Button2.configure(font="-family {Comic Sans MS} -size 16 -weight bold")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        photo_location = targetpath+"iconSlip.png"
        global _img02
        _img02 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img02)
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="flat")
        self.Button2.configure(text='''''')
        
        
        
        self.Button3 = tk.Button(self.top)
        self.Button3.place(relx=0.02, rely=0.9, height=56, width=136)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(background="#fff4ea")
        self.Button3.configure(font="-family {Comic Sans MS} -size 16 -weight bold")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        photo_location = targetpath+"iconback3.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button3.configure(image=_img2)
        self.Button3.configure(pady="0")
        self.Button3.configure(relief="flat")
        self.Button3.configure(text=''' Catalog''')
        self.Button3.configure(command=self.open_catalog)

        self.Label16 = tk.Label(self.top)
        self.Label16.place(relx=0.8, rely=0.8, height=110, width=120)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(anchor='w')
        self.Label16.configure(background="#fff4ea")
        self.Label16.configure(compound='left')
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#372a28")
        self.Label16.configure(highlightbackground="#ffc61a")
        self.Label16.configure(highlightcolor="black")
        photo_location = targetpath+"QR.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label16.configure(image=_img1)

        self.Label17 = tk.Label(self.top)
        self.Label17.place(relx=0.825, rely=0.957, height=21, width=86)
        self.Label17.configure(activebackground="#f9f9f9")
        self.Label17.configure(activeforeground="black")
        self.Label17.configure(anchor='w')
        self.Label17.configure(background="#fff4ea")
        self.Label17.configure(compound='left')
        self.Label17.configure(disabledforeground="#a3a3a3")
        self.Label17.configure(font="-family {Comic Sans MS} -size 12 -weight bold")
        self.Label17.configure(foreground="#372a28")
        self.Label17.configure(highlightbackground="#ffc61a")
        self.Label17.configure(highlightcolor="black")
        self.Label17.configure(text='''Scan Pay''')

        
       

        self.Label18 = tk.Label(self.top)
        self.Label18.place(relx=0.05, rely=0.571, height=21, width=230)
        self.Label18.configure(activebackground="#f9f9f9")
        self.Label18.configure(activeforeground="black")
        self.Label18.configure(anchor='w')
        self.Label18.configure(background="#fff4ea")
        self.Label18.configure(compound='left')
        self.Label18.configure(disabledforeground="#a3a3a3")
        self.Label18.configure(font="-family {Comic Sans MS} -size 16")
        self.Label18.configure(foreground="light yellow")
        self.Label18.configure(highlightbackground="#ffc61a")
        self.Label18.configure(highlightcolor="black")
        self.Label18.configure(text='''Member Information''')

   

def start_up():
    Resevation_support.main()

if __name__ == '__main__':
    Resevation_support.main()




