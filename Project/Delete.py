import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Delete_support
import Add_support
import Edit_support
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
        
    def open_Edit(self):
        self.top.destroy()
        Edit_support.main()
    
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

        top.geometry("800x700+461+37")
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
        self.Frame1.place(relx=0.0, rely=-0.033, relheight=1.059, relwidth=0.145)

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
        self.Label6.place(relx=0.0, rely=0.047, height=128, width=110)
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
        self.Button3.place(relx=0.086, rely=0.345, height=35, width=95)
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
        self.Button3.configure(command=self.open_Edit)

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

        self.Button5 = tk.Button(self.Frame1)
        self.Button5.place(relx=0.086, rely=0.897, height=35, width=95)
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
        self.Label1.place(relx=0.4, rely=0.033, height=72, width=278)
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
        self.Label1.configure(text='''Manage Shop''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.188, rely=0.167, height=48, width=220)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#fff4ea")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Arial Rounded MT Bold} -size 20 -weight bold")
        self.Label2.configure(foreground="#372a28")
        self.Label2.configure(highlightbackground="#ffc61a")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Delete Product''')
        
        self.Label09 = tk.Label(self.top)
        self.Label09.place(relx=0.47, rely=0.15, height=50, width=50)
        self.Label09.configure(activebackground="#f9f9f9")
        self.Label09.configure(activeforeground="black")
        self.Label09.configure(anchor='w')
        self.Label09.configure(background="#fff4ea")
        self.Label09.configure(compound='left')
        self.Label09.configure(disabledforeground="#a3a3a3")
        self.Label09.configure(foreground="#000000")
        self.Label09.configure(highlightbackground="#ffc61a")
        self.Label09.configure(highlightcolor="black")
        photo_location = targetpath+"icondelete.png"
        global _img001
        _img001 = tk.PhotoImage(file=photo_location)
        self.Label09.configure(image=_img001)

        self.Frame3 = tk.Frame(self.top)
        self.Frame3.place(relx=0.188, rely=0.233, relheight=0.109
                , relwidth=0.645)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#ffc61a")
        self.Frame3.configure(highlightbackground="#ffc61a")
        self.Frame3.configure(highlightcolor="black")

        self.Entry1 = tk.Entry(self.Frame3)
        self.Entry1.place(relx=0.368, rely=0.263, height=30, relwidth=0.388)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#ffc61a")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="blue")
        self.Entry1.configure(selectforeground="white")

        self.Label9 = tk.Label(self.Frame3)
        self.Label9.place(relx=0.769, rely=1.118, height=26, width=81)
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

        self.Button7 = tk.Button(self.Frame3)
        self.Button7.place(relx=0.775, rely=0.158, height=44, width=47)
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

        self.Label3 = tk.Label(self.Frame3)
        self.Label3.place(relx=0.116, rely=0.158, height=48, width=124)
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#ffc61a")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Arial Rounded MT Bold} -size 14")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Search Cat :''')

        self.Frame2 = tk.Frame(self.top)
        self.Frame2.place(relx=0.275, rely=0.371, relheight=0.354
                , relwidth=0.483)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ffc61a")

        self.Label4 = tk.Label(self.Frame2)
        self.Label4.place(relx=0.052, rely=0.085, height=121, width=103)
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#ffc61a")
        self.Label4.configure(compound='left')
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        photo_location = targetpath+"addcat.png"
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Label4.configure(image=_img3)

        self.Label5 = tk.Label(self.Frame2)
        self.Label5.place(relx=0.399, rely=0.085, height=32, width=189)
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#ffc61a")
        self.Label5.configure(compound='left')
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font="-family {Comic Sans MS} -size 12")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Cat ID :__________''')

        self.Label7 = tk.Label(self.Frame2)
        self.Label7.place(relx=0.435, rely=0.496, height=22, width=168)
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#ffc61a")
        self.Label7.configure(compound='left')
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font="-family {Comic Sans MS} -size 12")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(text='''Color :__________''')

        self.Label8 = tk.Label(self.Frame2)
        self.Label8.place(relx=0.44, rely=0.605, height=32, width=169)
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#ffc61a")
        self.Label8.configure(compound='left')
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(font="-family {Comic Sans MS} -size 12")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(text='''Price :__________''')

        self.Label10 = tk.Label(self.Frame2)
        self.Label10.place(relx=0.389, rely=0.218, height=32, width=219)
        self.Label10.configure(anchor='w')
        self.Label10.configure(background="#ffc61a")
        self.Label10.configure(compound='left')
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font="-family {Comic Sans MS} -size 12")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(text='''Species :__________''')

        self.Label11 = tk.Label(self.Frame2)
        self.Label11.place(relx=0.399, rely=0.335, height=33, width=168)
        self.Label11.configure(anchor='w')
        self.Label11.configure(background="#ffc61a")
        self.Label11.configure(compound='left')
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(font="-family {Comic Sans MS} -size 12")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(text='''Gender : __________''')

        self.Button1 = tk.Button(self.Frame2)
        self.Button1.place(relx=0.078, rely=0.685, height=34, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#372a28")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Comic Sans MS} -size 14 -weight bold")
        self.Button1.configure(foreground="white")
        self.Button1.configure(highlightbackground="#ffc61a")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Delete''')

def start_up():
    Delete_support.main()

if __name__ == '__main__':
    Delete_support.main()




