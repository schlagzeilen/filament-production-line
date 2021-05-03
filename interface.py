from tkinter import *
from tkinter import ttk
from classes import rot_axis ,lin_axis, maschine

from main import root, abzug


root.title("interface test")

mynotebook =ttk.Notebook(root)
mynotebook.pack()

# ----------------ABZUG FRAME-----------------

tab0_frame =Frame(mynotebook,bg="blue")
tab0_frame.pack(fill ="both",expand =1)
mynotebook.add(tab0_frame, text ="eins")

tab1_frame =Frame(mynotebook,bg="red")
tab1_frame.pack(fill ="both",expand =1)
mynotebook.add(tab1_frame, text ="zwai")

# ----------------ABZUG FRAME-----------------

abzug_control = LabelFrame(tab0_frame,text="ABZUG", bg="blue",width =12,height =12)
abzug_control.grid(row =0, column =0)

a_plus_eins =               Button(abzug_control, text="+1",    width =12,height =2,command = abzug.pause)
a_plus_zehntel =            Button(abzug_control, text="+0.1",  width =12,height =2)
a_plus_hundertstel =        Button(abzug_control, text="+0.01", width =12,height =2)
a_geschwindigkeit =         Text  (abzug_control,               width =12,height =2)
a_minus_eins =              Button(abzug_control, text="-1",    width =12,height =2,command =abzug.resume)
a_minus_zehntel =           Button(abzug_control, text="-0.1",  width =12,height =2)
a_minus_hundertstel =       Button(abzug_control, text="-0.01", width =12,height =2)

a_minus_hundertstel.        grid(row =0, column =0)
a_minus_zehntel.            grid(row =0, column =1)
a_minus_eins.               grid(row =0, column =2)
a_geschwindigkeit.          grid(row =0, column =3, sticky ="ew")
a_plus_eins.                grid(row =0, column =4)
a_plus_zehntel.             grid(row =0, column =5)
a_plus_hundertstel.         grid(row =0, column =6)

a_start_stop =              Button(abzug_control, text="START",width =12,height =2,command= abzug.start)
a_start_stop.               grid(row =1,column=3)

root.mainloop()
