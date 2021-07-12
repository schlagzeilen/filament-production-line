from tkinter import *
from tkinter import ttk
import tkinter as tk

class window():
    def __init__(self):
        self.root = Tk()
        self.root.title("interface test")

        self.mynotebook =ttk.Notebook(self.root)
        self.mynotebook.pack()

        # ----------------ABZUG FRAME-----------------

        self.tab0_frame =Frame(self.mynotebook,bg="blue")
        self.tab0_frame.pack(fill ="both",expand =1)
        self.mynotebook.add(self.tab0_frame, text ="eins")

        self.tab1_frame =Frame(self.mynotebook,bg="red")
        self.tab1_frame.pack(fill ="both",expand =1)
        self.mynotebook.add(self.tab1_frame, text ="zwai")

        # ----------------ABZUG FRAME-----------------

        self.abzug_control =            LabelFrame(self.tab0_frame,text="ABZUG", bg="blue",width =12,height =12)
        self.abzug_control.             grid(row =0, column =0)

        self.wicklung_control =         LabelFrame(self.tab0_frame,text="WICKLUNG",bg="yellow",width = 12,height =12)
        self.wicklung_control.          grid(row =1, column =0)

        self.y_control =                LabelFrame(self.tab0_frame,text="Y-ACHSE", bg="green",width = 12,height =12)
        self.y_control.                 grid(row =2,sticky="ew")
        self.center_frame =             Frame(self.y_control)
        self.center_frame.              pack()

    def run(self):
        self.root.mainloop()


class control_pannel():
    def __init__(self, control, achse, home=True):
        self.plus_eins =               Button(control, text="+10",    width =12,height =2, command =lambda: [achse.increment_speed(10)])
        self.plus_zehntel =            Button(control, text="+1",  width =12,height =2 , command =lambda: [achse.increment_speed(1)])
        self.plus_hundertstel =        Button(control, text="+0.1", width =12,height =2, command =lambda: [achse.increment_speed(0.1)])


        self.geschwindigkeit =         Text  (control,              width =12,height =2)
        self.minus_eins =              Button(control, text="-10",    width =12,height =2, command =lambda: [achse.increment_speed(-10)])
        self.minus_zehntel =           Button(control, text="-1",  width =12,height =2, command =lambda: [achse.increment_speed(-1)])
        self.minus_hundertstel =       Button(control, text="-0.1", width =12,height =2, command =lambda: [achse.increment_speed(-0.1)])

        self.minus_hundertstel.        grid(row =0, column =0)
        self.minus_zehntel.            grid(row =0, column =1)
        self.minus_eins.               grid(row =0, column =2)
        self.geschwindigkeit.          grid(row =0, column =3, sticky ="ew")
        self.plus_eins.                grid(row =0, column =4)
        self.plus_zehntel.             grid(row =0, column =5)
        self.plus_hundertstel.         grid(row =0, column =6)
        self.ich =achse                 #evtl unnötig vllt kann man auch einfach achse übergeben


        self.btn_text = tk.StringVar() # tkinter textvariable für den text des startbuttons, da dieser sich ändern wird
        self.start_stop =              Button(control, textvariable=self.btn_text,width =12,height =2,command= lambda:[achse.start(),self.change_button_start_stop(self.ich)]) #hier werden zwei funktionen gleichzeitig übergeben.
        self.btn_text.set("START")                                                                                                                                              #change button start stop soll dabei den Buttontext und den command ändern


        self.start_stop.               grid(row =1,column=3)
        i = int() # TODO i ist nur stellvertretend für die variable die geändert wird wenn der radiobutton gedrückt wird
        self.regelung =                  Radiobutton(control, text="Regelung", variable=i, value=1, width =12,height =2 )
        self.regelung.                   grid(row =1,column=4)

        if home:
            self.home =                 Button(control, text="HOME",       width =12,height =2)
            self.home.                  grid(row=1, column =2 )

    def change_button_start_stop(self, achse):
        print("ich wurde aufgerufen")
        if self.btn_text.get() =="START": #checkt was im button steht
            self.start_stop.configure(command = lambda:[self.ich.pause(),self.change_button_start_stop(self.ich)]) #ändert button configuration
            self.btn_text.set("PAUSE")#ändert namen

        elif self.btn_text.get() =="PAUSE":
            print("geschafft")
            self.start_stop.configure(command = lambda:[self.ich.resume(),self.change_button_start_stop(self.ich)])
            self.btn_text.set("RESUME")

        elif self.btn_text.get() =="RESUME":
            self.start_stop.configure(command = lambda:[self.ich.pause(),self.change_button_start_stop(self.ich)])
            self.btn_text.set("PAUSE")
