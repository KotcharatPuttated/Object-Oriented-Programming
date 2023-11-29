import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Edit_support
import Add_support
import Delete_support
import Login_support
import admin_support

import os
userpath = os.path.expanduser("~")
targetpath = userpath+"/Downloads/OOP(1)/OOP/GUi/Login/image/"

class Toplevel1:
    
    def open_profileAdmin(self):
        self.top.destroy()
        admin_support.main()
    
    def open_add(self):
        self.top.destroy()
        Add_support.main()
        
    def open_delete(self):
        self.top.destroy()
        Delete_support.main()
    
    def open_login(self):
        self.top.destroy()
        Login_support.main()
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffc61a'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffc61a' # X11 color: 'gray85'
        _ana1color = '#ffc61a' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("800x600+459+70")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("JONG NONG")
        top.configure(background="#fff4ea")
        top.configure(highlightbackground="#ffc61a")
        top.configure(highlightcolor="black")

        self.top = top
        
        self.ProfileAdmin = tk.Button(self.top)
        self.ProfileAdmin.place(relx=0.913, rely=0.029, height=50, width=50)
        self.ProfileAdmin.configure(background="#fff4ea")
        self.ProfileAdmin.configure(compound='left')
        self.ProfileAdmin.configure(foreground="#fff4ea")
        self.ProfileAdmin.configure(font="-family {Comic Sans MS} -size 18 -weight bold")
        self.ProfileAdmin.configure(foreground="#372a28")
        self.ProfileAdmin.configure(text='''''')
        photo_location = targetpath+"admiticon50.png"
        global _img003
        _img003 = tk.PhotoImage(file=photo_location)
        self.ProfileAdmin.configure(image=_img003)
        self.ProfileAdmin.configure(pady="0")
        self.ProfileAdmin.configure(relief="flat")
        self.ProfileAdmin.configure(command=self.open_profileAdmin)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.0, rely=-0.033, relheight=1.058, relwidth=0.145)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffc61a")
        self.Frame1.configure(highlightbackground="#ffc61a")
        self.Frame1.configure(highlightcolor="black")

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.086, rely=0.283, height=35, width=95)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#372a28")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Arial Rounded MT Bold} -size 13")
        self.Button2.configure(foreground="white")
        self.Button2.configure(highlightbackground="#ffc61a")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Add''')
        self.Button2.configure(command=self.open_add)

        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.0, rely=0.047, height=110, width=110)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#ffc61a")
        self.Label6.configure(compound='left')
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#ffc61a")
        self.Label6.configure(highlightcolor="black")
        photo_location = targetpath+"logo110x110.png"
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label6.configure(image=_img0)
        self.Label6.configure(text='''Label''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.086, rely=0.346, height=35, width=95)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#372a28")
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Arial Rounded MT Bold} -size 13")
        self.Button3.configure(foreground="white")
        self.Button3.configure(highlightbackground="#ffc61a")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Edit''')
        

        self.Button4 = tk.Button(self.Frame1)
        self.Button4.place(relx=0.086, rely=0.409, height=35, width=95)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#372a28")
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Arial Rounded MT Bold} -size 13")
        self.Button4.configure(foreground="white")
        self.Button4.configure(highlightbackground="#ffc61a")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Delete''')
        self.Button4.configure(command=self.open_delete)


        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.086, rely=0.898, height=35, width=95)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#372a28")
        self.Button5.configure(compound='left')
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font="-family {Arial Rounded MT Bold} -size 13")
        self.Button5.configure(foreground="white")
        self.Button5.configure(highlightbackground="#ffc61a")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Logout''')
        self.Button5.configure(command=self.open_login)

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.4, rely=0.033, height=61, width=278)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#fff4ea")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Arial Rounded MT Bold} -size 30")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#ffc61a")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Manage Shop''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.175, rely=0.183, height=31, width=200)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#fff4ea")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial Rounded MT Bold} -size 20 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#ffc61a")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Edit Product''')
        
        self.Label09 = tk.Label(self.top)
        self.Label09.place(relx=0.42, rely=0.16, height=50, width=50)
        self.Label09.configure(activebackground="#f9f9f9")
        self.Label09.configure(activeforeground="black")
        self.Label09.configure(anchor='w')
        self.Label09.configure(background="#fff4ea")
        self.Label09.configure(compound='left')
        self.Label09.configure(disabledforeground="#a3a3a3")
        self.Label09.configure(foreground="#000000")
        self.Label09.configure(highlightbackground="#ffc61a")
        self.Label09.configure(highlightcolor="black")
        photo_location = targetpath+"iconedit.png"
        global _img001
        _img001 = tk.PhotoImage(file=photo_location)
        self.Label09.configure(image=_img001)

        self.Frame3 = tk.Frame(self.top)
        self.Frame3.place(relx=0.175, rely=0.25, relheight=0.492, relwidth=0.795)

        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#ffc61a")
        self.Frame3.configure(highlightbackground="#ffc61a")
        self.Frame3.configure(highlightcolor="black")

        self.Label3 = tk.Label(self.Frame3)
        self.Label3.place(relx=0.126, rely=0.092, height=30, width=154)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#ffc61a")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#ffc61a")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Search Cat ID :''')

        self.Entry1 = tk.Entry(self.Frame3)
        self.Entry1.place(relx=0.377, rely=0.092, height=30, relwidth=0.314)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#ffc61a")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Label4 = tk.Label(self.Frame3)
        self.Label4.place(relx=0.425, rely=0.39, height=31, width=94)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#ffc61a")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#ffc61a")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Gender :''')

        self.Label5 = tk.Label(self.Frame3)
        self.Label5.place(relx=0.047, rely=0.234, height=31, width=104)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#ffc61a")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#ffc61a")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Species :''')

        self.Label7 = tk.Label(self.Frame3)
        self.Label7.place(relx=0.456, rely=0.234, height=31, width=74)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#ffc61a")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#ffc61a")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Color :''')

        self.Label8 = tk.Label(self.Frame3)
        self.Label8.place(relx=0.079, rely=0.39, height=31, width=74)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#ffc61a")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#ffc61a")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Price :''')

        self.Label9 = tk.Label(self.Frame3)
        self.Label9.place(relx=0.786, rely=0.39, height=100, width=100)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#ffc61a")
        self.Label9.configure(compound='left')
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#ffc61a")
        self.Label9.configure(highlightcolor="black")
        photo_location = targetpath+"addcat.png"
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.Label9.configure(image=_img1)

        self.Button1 = tk.Button(self.Frame3)
        self.Button1.place(relx=0.786, rely=0.725, height=24, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#372a28")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Arial Rounded MT Bold} -size 12")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#ffc61a")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Image''')

        self.Label10 = tk.Label(self.Frame3)
        self.Label10.place(relx=0.204, rely=0.234, height=24, width=143)
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#ffc61a")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''_______________________''')

        self.Label11 = tk.Label(self.Frame3)
        self.Label11.place(relx=0.582, rely=0.234, height=24, width=122)
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#ffc61a")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''___________________''')

        self.Label12 = tk.Label(self.Frame3)
        self.Label12.place(relx=0.204, rely=0.39, height=24, width=114)
        self.Label12.configure(anchor='w')
        self.Label12.configure(background="#ffc61a")
        self.Label12.configure(compound='left')
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(text='''_____________''')

        self.Label13 = tk.Label(self.Frame3)
        self.Label13.place(relx=0.566, rely=0.39, height=24, width=114)
        self.Label13.configure(anchor='w')
        self.Label13.configure(background="#ffc61a")
        self.Label13.configure(compound='left')
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''__________''')

        self.Button7 = tk.Button(self.Frame3)
        self.Button7.place(relx=0.708, rely=0.068, height=44, width=47)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#ffc61a")
        self.Button7.configure(compound='left')
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#ffc61a")
        self.Button7.configure(highlightcolor="black")
        photo_location = targetpath+"search.png"
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button7.configure(image=_img2)
        self.Button7.configure(pady="0")
        self.Button7.configure(relief="flat")

        self.Button6 = tk.Button(self.top)
        self.Button6.place(relx=0.488, rely=0.65, height=44, width=127)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#372a28")
        self.Button6.configure(compound='left')
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font="-family {Arial Rounded MT Bold} -size 16")
        self.Button6.configure(foreground="white")
        self.Button6.configure(highlightbackground="#ffc61a")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Edit Cat''')

def start_up():
    Edit_support.main()

if __name__ == '__main__':
    Edit_support.main()




