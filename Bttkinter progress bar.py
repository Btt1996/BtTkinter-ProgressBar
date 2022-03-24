from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
scr=Tk()
scr.title("Progressbar")
scr.geometry('5000x1000')
s = ttk.Style()
s.theme_use('default')
s.configure("black.Horizontal.TProgressbar", background='red')
b=Button(scr,text="Increase",fg="black",bg="green",font=('Time','13','bold'),command=lambda:increase())
b.place(x=550,y=450)
b=Button(scr,text="Decrease",fg="black",bg="red",font=('Time','13','bold'),command=lambda:decrease())
b.place(x=750,y=450)
bar = Progressbar(scr, length=400, s='black.Horizontal.TProgressbar')
bar['value'] = 20
bar.place(x=500,y=400)

def increase():
    if bar['value']<100:
        bar['value']=bar['value']+10
    if bar['value']<=30:
       s.configure("black.Horizontal.TProgressbar", background='red')
    elif bar['value']>30 and bar['value']<=60:
       s.configure("black.Horizontal.TProgressbar", background='orange')
    elif bar['value']>60 and bar['value']<=80:
       s.configure("black.Horizontal.TProgressbar", background='yellow')
    elif bar['value']>80:
       s.configure("black.Horizontal.TProgressbar", background='green')

def decrease():
    if bar['value']>0:
        bar['value']=bar['value']-10
    if bar['value']<=30:
        s.configure("black.Horizontal.TProgressbar", background='red')
    elif bar['value']>30 and bar['value']<=60:
       s.configure("black.Horizontal.TProgressbar", background='orange')
    elif bar['value']>60 and bar['value']<=80:
       s.configure("black.Horizontal.TProgressbar", background='yellow')
    elif bar['value']>80:
       s.configure("black.Horizontal.TProgressbar", background='green')
