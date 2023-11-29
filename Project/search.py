import imp
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import search_support
import CatalogResults_support
import Login_support
import ProfileCus_support

import os
userpath = os.path.expanduser("~")
targetpath = userpath+"/Downloads/OOP(1)/OOP/GUi/Login/image/"

class Toplevel1:
        
        def open_login(self):
                self.top.destroy()
                Login_support.main()
                
        def open_profile(self):
                self.top.destroy()
                ProfileCus_support.main()
        
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
                self.style = ttk.Style()
                if sys.platform == "win32":
                        self.style.theme_use('winnative')
                        self.style.configure('.',background=_bgcolor)
                        self.style.configure('.',foreground=_fgcolor)
                        self.style.configure('.',font="TkDefaultFont")
                        self.style.map('.',background=
                        [('selected', _compcolor), ('active',_ana2color)])
                top.geometry("800x700+411+7")
                top.minsize(120, 1)
                top.maxsize(1540, 845)
                top.resizable(1,  1)
                top.title("JONG NONG")
                top.configure(background="#fff4ea")

                self.top = top
                
                self.Profile = tk.Button(self.top)
                self.Profile.place(relx=0.913, rely=0.029, height=50, width=50)
                self.Profile.configure(background="#d9d9d9")
                self.Profile.configure(compound='left')
                self.Profile.configure(foreground="#000000")
                photo_location = targetpath+"profile50.png"
                global _img4
                _img4 = tk.PhotoImage(file=photo_location)
                self.Profile.configure(image=_img4)
                self.Profile.configure(pady="0")
                self.Profile.configure(relief="flat")
                self.Profile.configure(state='active')
                self.Profile.configure(command=self.open_profile)
                
                self.combobox = tk.StringVar()
                self.combobox2 = tk.StringVar()
                self.combobox3 = tk.StringVar()
                self.combobox4 = tk.StringVar()
                self.combobox5 = tk.StringVar()
                

                self.Label1 = tk.Label(self.top)
                self.Label1.place(relx=0.28, rely=0.043, height=62, width=500)
                self.Label1.configure(anchor='w')
                self.Label1.configure(background="#fff4ea")
                self.Label1.configure(compound='left')
                self.Label1.configure(disabledforeground="#a3a3a3")
                self.Label1.configure(font="-family {Arial Rounded MT Bold} -size 45")
                self.Label1.configure(foreground="#440a00")
                self.Label1.configure(text='''JONG NONG''')

                self.Label2 = tk.Label(self.top)
                self.Label2.place(relx=0.350, rely=0.129, height=61, width=310)
                self.Label2.configure(anchor='w')
                self.Label2.configure(background="#fff4ea")
                self.Label2.configure(compound='left')
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Comic Sans MS} -size 24")
                self.Label2.configure(foreground="#372a28")
                self.Label2.configure(text='''" Search Cat Shop "''')
                
                self.Label06 = tk.Label(self.top)
                self.Label06.place(relx=0.1, rely=0.03, height=130, width=130)
                self.Label06.configure(activebackground="#f9f9f9")
                self.Label06.configure(activeforeground="black")
                self.Label06.configure(anchor='w')
                self.Label06.configure(background="#fff4ea")
                self.Label06.configure(compound='left')
                self.Label06.configure(disabledforeground="#a3a3a3")
                self.Label06.configure(foreground="#440a00")
                self.Label06.configure(highlightbackground="#ffc61a")
                self.Label06.configure(highlightcolor="black")
                photo_location = targetpath+"logo130x130.png"
                global _img0
                _img0 = tk.PhotoImage(file=photo_location)
                self.Label06.configure(image=_img0)
                self.Label06.configure(text='''''')

                self.Frame1 = tk.Frame(self.top)
                self.Frame1.place(relx=0.113, rely=0.257, relheight=0.536
                        , relwidth=0.795)
                self.Frame1.configure(relief='groove')
                self.Frame1.configure(borderwidth="2")
                self.Frame1.configure(relief="groove")
                self.Frame1.configure(background="#ffc61a")

                self.TCombobox1 = ttk.Combobox(self.Frame1)
                
                self.TCombobox1['values'] = ("Male", "Female")
                self.TCombobox1.place(relx=0.189, rely=0.187, relheight=0.08
                        , relwidth=0.22)
                self.TCombobox1.configure(textvariable=self.combobox)
                self.TCombobox1.configure(takefocus="")

                self.TCombobox2 = ttk.Combobox(self.Frame1)
                self.TCombobox2['values'] = ("White", "Black", "Brown", "Orange", "Grey")
                self.TCombobox2.place(relx=0.629, rely=0.187, relheight=0.08
                        , relwidth=0.22)
                self.TCombobox2.configure(textvariable=self.combobox2)
                self.TCombobox2.configure(takefocus="")

                self.TCombobox3 = ttk.Combobox(self.Frame1)
                self.TCombobox3['values'] = ("American Short Hair", "Scottish Fold", "Persian", "Maine Coon", "Siamese")
                self.TCombobox3.place(relx=0.189, rely=0.427, relheight=0.08
                        , relwidth=0.22)
                self.TCombobox3.configure(textvariable=self.combobox3)
                self.TCombobox3.configure(takefocus="")

                self.Label3 = tk.Label(self.Frame1)
                self.Label3.place(relx=0.063, rely=0.16, height=51, width=74)
                self.Label3.configure(anchor='w')
                self.Label3.configure(background="#ffc61a")
                self.Label3.configure(compound='left')
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(font="-family {Comic Sans MS} -size 16")
                self.Label3.configure(foreground="#440a00")
                self.Label3.configure(text='''Gender''')

                self.Label4 = tk.Label(self.Frame1)
                self.Label4.place(relx=0.519, rely=0.187, height=31, width=64)
                self.Label4.configure(anchor='w')
                self.Label4.configure(background="#ffc61a")
                self.Label4.configure(compound='left')
                self.Label4.configure(disabledforeground="#a3a3a3")
                self.Label4.configure(font="-family {Comic Sans MS} -size 16")
                self.Label4.configure(foreground="#440a00")
                self.Label4.configure(text='''Color''')

                self.Label5 = tk.Label(self.Frame1)
                self.Label5.place(relx=0.05, rely=0.427, height=31, width=80)
                self.Label5.configure(anchor='w')
                self.Label5.configure(background="#ffc61a")
                self.Label5.configure(compound='left')
                self.Label5.configure(disabledforeground="#a3a3a3")
                self.Label5.configure(font="-family {Comic Sans MS} -size 16")
                self.Label5.configure(foreground="#440a00")
                self.Label5.configure(text='''Species''')

                self.Label6 = tk.Label(self.Frame1)
                self.Label6.place(relx=0.519, rely=0.4, height=41, width=53)
                self.Label6.configure(anchor='w')
                self.Label6.configure(background="#ffc61a")   
                self.Label6.configure(compound='left')
                self.Label6.configure(disabledforeground="#a3a3a3")
                self.Label6.configure(font="-family {Comic Sans MS} -size 16")
                self.Label6.configure(foreground="#440a00")
                self.Label6.configure(text='''Price''')

                self.TCombobox4 = ttk.Combobox(self.Frame1)
                self.TCombobox4['values'] = ("1,000", "1,500", "2,000", "2,500", "3,000")
                self.TCombobox4.place(relx=0.629, rely=0.427, relheight=0.08
                        , relwidth=0.157)
                self.TCombobox4.configure(textvariable=self.combobox4)
                self.TCombobox4.configure(takefocus="")

                self.TCombobox5 = ttk.Combobox(self.Frame1)
                self.TCombobox5['values'] = ("10,000", "15,000", "20,000", "25,000", "30,000")
                self.TCombobox5.place(relx=0.818, rely=0.427, relheight=0.08
                        , relwidth=0.157)
                self.TCombobox5.configure(textvariable=self.combobox5)
                self.TCombobox5.configure(takefocus="")

                self.Label7 = tk.Label(self.Frame1)
                self.Label7.place(relx=0.723, rely=0.347, height=21, width=34)
                self.Label7.configure(anchor='w')
                self.Label7.configure(background="#ffc61a")
                self.Label7.configure(compound='left')
                self.Label7.configure(disabledforeground="#a3a3a3")
                self.Label7.configure(foreground="#440a00")
                self.Label7.configure(text='''MIN''')

                self.Label8 = tk.Label(self.Frame1)
                self.Label8.place(relx=0.912, rely=0.347, height=21, width=34)
                self.Label8.configure(anchor='w')
                self.Label8.configure(background="#ffc61a")
                self.Label8.configure(compound='left')
                self.Label8.configure(disabledforeground="#a3a3a3")
                self.Label8.configure(foreground="#440a00")
                self.Label8.configure(text='''MAX''')

                self.Button1 = tk.Button(self.Frame1)
                self.Button1.place(relx=0.33, rely=0.667, height=44, width=200)
                self.Button1.configure(activebackground="#ececec")
                self.Button1.configure(activeforeground="#440a00")
                self.Button1.configure(background="#372a28")
                self.Button1.configure(compound='left')
                self.Button1.configure(disabledforeground="#a3a3a3")
                self.Button1.configure(font="-family {Comic Sans MS} -size 22 -weight bold")
                self.Button1.configure(foreground="white")
                self.Button1.configure(highlightbackground="#ffc61a")
                self.Button1.configure(highlightcolor="black")
                self.Button1.configure(pady="0")
                self.Button1.configure(text='''Search''')
                self.Button1.configure(command=self.open_catalog)
                
                self.Button2 = tk.Button(self.top)
                self.Button2.place(relx=-0.003, rely=0.9, height=56, width=136)
                self.Button2.configure(activebackground="#ececec")
                self.Button2.configure(activeforeground="#000000")
                self.Button2.configure(background="#fff4ea")
                self.Button2.configure(compound='left')
                self.Button2.configure(disabledforeground="#a3a3a3")
                self.Button2.configure(font="-family {Comic Sans MS} -size 16 -weight bold")
                self.Button2.configure(foreground="#000000")
                self.Button2.configure(highlightbackground="#d9d9d9")
                self.Button2.configure(highlightcolor="black")
                photo_location = targetpath+"iconlogout50.png"
                global _img2
                _img2 = tk.PhotoImage(file=photo_location)
                self.Button2.configure(image=_img2)
                self.Button2.configure(pady="0")
                self.Button2.configure(relief="flat")
                self.Button2.configure(text='''Logout''')
                self.Button2.configure(command=self.open_login)

                

def start_up():
    search_support.main()

if __name__ == '__main__':
    search_support.main()




