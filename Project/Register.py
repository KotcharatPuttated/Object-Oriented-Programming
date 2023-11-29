import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Register_support
import search_support

import os
userpath = os.path.expanduser("~")
targetpath = userpath+"/Downloads/OOP(1)/OOP/GUi/Login/image/"


class Toplevel1:
        def open_search(self):
                self.top.destroy()
                search_support.main()
        def __init__(self, top=None):
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
                
                top.geometry("800x700+443+45")
                top.minsize(120, 1)
                top.maxsize(1540, 845)
                top.resizable(1,  1)
                top.title("JONG NONG")
                top.configure(background="#fff4ea")
                top.configure(highlightbackground="#d9d9d9")
                top.configure(highlightcolor="black")

                self.top = top
                self.che58 = tk.IntVar()
                self.che59 = tk.IntVar()
                
                self.Label3 = tk.Label(self.top)
                self.Label3.place(relx=0.02, rely=0.02, height=110, width=111)
                self.Label3.configure(activebackground="#f9f9f9")
                self.Label3.configure(activeforeground="black")
                self.Label3.configure(anchor='w')
                self.Label3.configure(background="#fff4ea")
                self.Label3.configure(compound='left')
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(foreground="#440a00")
                self.Label3.configure(highlightbackground="#ffc61a")
                self.Label3.configure(highlightcolor="black")
                photo_location = targetpath+"logo110x110.png"
                global _img1
                _img1 = tk.PhotoImage(file=photo_location)
                self.Label3.configure(image=_img1)
                self.Label3.configure(text='''Label''')

                self.Frame1 = tk.Frame(self.top)
                self.Frame1.place(relx=0.05, rely=0.2, relheight=0.7, relwidth=0.895)

                self.Frame1.configure(relief='groove')
                self.Frame1.configure(borderwidth="2")
                self.Frame1.configure(relief="groove")
                self.Frame1.configure(background="#ffc61a")
                self.Frame1.configure(highlightbackground="#d9d9d9")
                self.Frame1.configure(highlightcolor="black")

                self.Entry001 = tk.Entry(self.Frame1)
                self.Entry001.place(relx=0.531, rely=0.155, relheight=0.078, relwidth=0.419)
                self.Entry001.configure(background="#372a28")
                self.Entry001.configure(font="TkFixedFont")
                self.Entry001.configure(foreground="white")

                self.Entry002 = tk.Entry(self.Frame1)
                self.Entry002.place(relx=0.042, rely=0.351, relheight=0.078, relwidth=0.419)
                self.Entry002.configure(background="#372a28")
                self.Entry002.configure(font="TkFixedFont")
                self.Entry002.configure(foreground="white")
                

                self.TEntry3 = ttk.Entry(self.Frame1)
                self.TEntry3.place(relx=0.531, rely=0.351, relheight=0.078
                        , relwidth=0.419)
                self.TEntry3.configure(takefocus="")
                self.TEntry3.configure(cursor="ibeam")
                
                self.Entry003 = tk.Entry(self.Frame1)
                self.Entry003.place(relx=0.531, rely=0.351, relheight=0.078, relwidth=0.419)
                self.Entry003.configure(background="#372a28")
                self.Entry003.configure(font="TkFixedFont")
                self.Entry003.configure(foreground="white")

        
                self.Entry004 = tk.Entry(self.Frame1)
                self.Entry004.place(relx=0.042, rely=0.155, relheight=0.078, relwidth=0.419)
                self.Entry004.configure(background="#372a28")
                self.Entry004.configure(font="TkFixedFont")
                self.Entry004.configure(foreground="white")

                
                

                self.Entry1 = tk.Entry(self.Frame1)
                self.Entry1.place(relx=0.531, rely=0.523, height=80, relwidth=0.419)
                self.Entry1.configure(background="#372a28")
                self.Entry1.configure(disabledforeground="#a3a3a3")
                self.Entry1.configure(font="TkFixedFont")
                self.Entry1.configure(foreground="white")
                self.Entry1.configure(highlightbackground="#d9d9d9")
                self.Entry1.configure(highlightcolor="black")
                self.Entry1.configure(insertbackground="black")
                self.Entry1.configure(selectbackground="blue")
                self.Entry1.configure(selectforeground="#372a28")

                self.Entry2 = tk.Entry(self.Frame1)
                self.Entry2.place(relx=0.042, rely=0.523, height=40, relwidth=0.419)
                self.Entry2.configure(background="#372a28")
                self.Entry2.configure(font="TkFixedFont")
                self.Entry2.configure(foreground="white")
                
                self.Checkbutton1 = tk.Checkbutton(self.Frame1)
                self.Checkbutton1.place(relx=0.14, rely=0.678, relheight=0.087, relwidth=0.113)
                self.Checkbutton1.configure(activebackground="#ececec")
                self.Checkbutton1.configure(activeforeground="#000000")
                self.Checkbutton1.configure(anchor='w')
                self.Checkbutton1.configure(background="#ffc61a")
                self.Checkbutton1.configure(compound='left')
                self.Checkbutton1.configure(disabledforeground="#a3a3a3")
                self.Checkbutton1.configure(font="-family {Comic Sans MS} -size 14")
                self.Checkbutton1.configure(foreground="#440a00")
                self.Checkbutton1.configure(highlightbackground="#d9d9d9")
                self.Checkbutton1.configure(highlightcolor="black")
                self.Checkbutton1.configure(justify='left')
                self.Checkbutton1.configure(text='''Male''')
                self.Checkbutton1.configure(variable=self.che58)

                self.Checkbutton2 = tk.Checkbutton(self.Frame1)
                self.Checkbutton2.place(relx=0.265, rely=0.698, relheight=0.048
                        , relwidth=0.127)
                self.Checkbutton2.configure(activebackground="#ececec")
                self.Checkbutton2.configure(activeforeground="#000000")
                self.Checkbutton2.configure(anchor='w')
                self.Checkbutton2.configure(background="#ffc61a")
                self.Checkbutton2.configure(compound='left')
                self.Checkbutton2.configure(disabledforeground="#a3a3a3")
                self.Checkbutton2.configure(font="-family {Comic Sans MS} -size 14")
                self.Checkbutton2.configure(foreground="#440a00")
                self.Checkbutton2.configure(highlightbackground="#d9d9d9")
                self.Checkbutton2.configure(highlightcolor="black")
                self.Checkbutton2.configure(justify='left')
                self.Checkbutton2.configure(text='''Female''')
                self.Checkbutton2.configure(variable=self.che59)

                self.Button1 = tk.Button(self.Frame1)
                self.Button1.place(relx=0.35, rely=0.795, height=44, width=220)
                self.Button1.configure(activebackground="#ececec")
                self.Button1.configure(activeforeground="#000000")
                self.Button1.configure(background="#372a28")
                self.Button1.configure(compound='left')
                self.Button1.configure(disabledforeground="#a3a3a3")
                self.Button1.configure(font="-family {Comic Sans MS} -size 20")
                self.Button1.configure(foreground="white")
                self.Button1.configure(highlightbackground="#d9d9d9")
                self.Button1.configure(highlightcolor="black")
                self.Button1.configure(pady="0")
                self.Button1.configure(text='''Register''')
                self.Button1.configure(command=self.open_search)

                self.Label2 = tk.Label(self.Frame1)
                self.Label2.place(relx=0.056, rely=0.097, height=21, width=123)
                self.Label2.configure(activebackground="#f9f9f9")
                self.Label2.configure(activeforeground="black")
                self.Label2.configure(anchor='w')
                self.Label2.configure(background="#ffc61a")
                self.Label2.configure(compound='left')
                self.Label2.configure(disabledforeground="#a3a3a3")
                self.Label2.configure(font="-family {Comic Sans MS} -size 14")
                self.Label2.configure(foreground="#440a00")
                self.Label2.configure(highlightbackground="#d9d9d9")
                self.Label2.configure(highlightcolor="black")
                self.Label2.configure(text='''Full Name :''')

                self.Label3 = tk.Label(self.Frame1)
                self.Label3.place(relx=0.531, rely=0.097, height=21, width=84)
                self.Label3.configure(activebackground="#f9f9f9")
                self.Label3.configure(activeforeground="black")
                self.Label3.configure(anchor='w')
                self.Label3.configure(background="#ffc61a")
                self.Label3.configure(compound='left')
                self.Label3.configure(disabledforeground="#a3a3a3")
                self.Label3.configure(font="-family {Comic Sans MS} -size 14")
                self.Label3.configure(foreground="#440a00")
                self.Label3.configure(highlightbackground="#d9d9d9")
                self.Label3.configure(highlightcolor="black")
                self.Label3.configure(text='''Email :''')

                self.Label4 = tk.Label(self.Frame1)
                self.Label4.place(relx=0.042, rely=0.306, height=21, width=124)
                self.Label4.configure(activebackground="#f9f9f9")
                self.Label4.configure(activeforeground="black")
                self.Label4.configure(anchor='w')
                self.Label4.configure(background="#ffc61a")
                self.Label4.configure(compound='left')
                self.Label4.configure(disabledforeground="#a3a3a3")
                self.Label4.configure(font="-family {Comic Sans MS} -size 14")
                self.Label4.configure(foreground="#440a00")
                self.Label4.configure(highlightbackground="#d9d9d9")
                self.Label4.configure(highlightcolor="black")
                self.Label4.configure(text='''Username :''')

                self.Label5 = tk.Label(self.Frame1)
                self.Label5.place(relx=0.531, rely=0.308, height=21, width=97)
                self.Label5.configure(activebackground="#f9f9f9")
                self.Label5.configure(activeforeground="black")
                self.Label5.configure(anchor='w')
                self.Label5.configure(background="#ffc61a")
                self.Label5.configure(compound='left')
                self.Label5.configure(disabledforeground="#a3a3a3")
                self.Label5.configure(font="-family {Comic Sans MS} -size 14")
                self.Label5.configure(foreground="#440a00")
                self.Label5.configure(highlightbackground="#d9d9d9")
                self.Label5.configure(highlightcolor="black")
                self.Label5.configure(text='''Password :''')

                self.Label6 = tk.Label(self.Frame1)
                self.Label6.place(relx=0.042, rely=0.479, height=21, width=164)
                self.Label6.configure(activebackground="#f9f9f9")
                self.Label6.configure(activeforeground="black")
                self.Label6.configure(anchor='w')
                self.Label6.configure(background="#ffc61a")
                self.Label6.configure(compound='left')
                self.Label6.configure(disabledforeground="#a3a3a3")
                self.Label6.configure(font="-family {Comic Sans MS} -size 14")
                self.Label6.configure(foreground="#440a00")
                self.Label6.configure(highlightbackground="#d9d9d9")
                self.Label6.configure(highlightcolor="black")
                self.Label6.configure(text='''Phone Number :''')

                self.Label7 = tk.Label(self.Frame1)
                self.Label7.place(relx=0.531, rely=0.479, height=21, width=104)
                self.Label7.configure(activebackground="#f9f9f9")
                self.Label7.configure(activeforeground="black")
                self.Label7.configure(anchor='w')
                self.Label7.configure(background="#ffc61a")
                self.Label7.configure(compound='left')
                self.Label7.configure(disabledforeground="#a3a3a3")
                self.Label7.configure(font="-family {Comic Sans MS} -size 14")
                self.Label7.configure(foreground="#440a00")
                self.Label7.configure(highlightbackground="#d9d9d9")
                self.Label7.configure(highlightcolor="black")
                self.Label7.configure(text='''Address :''')

                self.Label8 = tk.Label(self.Frame1)
                self.Label8.place(relx=0.209, rely=0.64, height=21, width=93)
                self.Label8.configure(activebackground="#f9f9f9")
                self.Label8.configure(activeforeground="black")
                self.Label8.configure(anchor='w')
                self.Label8.configure(background="#ffc61a")
                self.Label8.configure(compound='left')
                self.Label8.configure(disabledforeground="#a3a3a3")
                self.Label8.configure(font="-family {Comic Sans MS} -size 14")
                self.Label8.configure(foreground="#440a00")
                self.Label8.configure(highlightbackground="#d9d9d9")
                self.Label8.configure(highlightcolor="black")
                self.Label8.configure(text='''GENDER''')

                self.Label1 = tk.Label(self.top)
                self.Label1.place(relx=0.2, rely=0.06, height=60, width=320)
                self.Label1.configure(activebackground="#f9f9f9")
                self.Label1.configure(activeforeground="black")
                self.Label1.configure(anchor='w')
                self.Label1.configure(background="#fff4ea")
                self.Label1.configure(compound='left')
                self.Label1.configure(disabledforeground="#a3a3a3")
                self.Label1.configure(font="-family {Arial Rounded MT Bold} -size 38")
                self.Label1.configure(foreground="#440a00")
                self.Label1.configure(highlightbackground="#d9d9d9")
                self.Label1.configure(highlightcolor="black")
                self.Label1.configure(text='''Registration''')
                
                # self.Label06 = tk.Label(self.top)
                # self.Label06.place(relx=0.45, rely=0.832, height=110, width=120)
                # self.Label06.configure(anchor='w')
                # self.Label06.configure(background="#fff4ea")
                # self.Label06.configure(compound='left')
                # self.Label06.configure(disabledforeground="#a3a3a3")
                # self.Label06.configure(foreground="#000000")
                # photo_location = targetpath+"logo110x110.png"
                # global _img0
                # _img0 = tk.PhotoImage(file=photo_location)
                # self.Label06.configure(image=_img0)
                # self.Label06.configure(text='''''')
                


                self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
                top.configure(menu = self.menubar)

def start_up():
    Register_support.main()

if __name__ == '__main__':
    Register_support.main()




