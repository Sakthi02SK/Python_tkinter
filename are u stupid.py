from tkinter import *
from turtle import onclick
import random as rc
r=Tk()
#r.attributes("-fullscreen",True)
r.geometry("1366x768")
r.title("My creation")
r.config(bg="white")
label=Label(r, text="Are You Stupid?",fg="black",bg="white",font=("Segoe Script",80))
label.pack(padx=50,pady=100)
def yes():
    s=Tk()
    #s.attributes("-fullscreen",True)
    s.geometry("1366x768")
    s.title("Truth")
    l=Label(s, text="I knew it :)",font=("Segoe Script",80))
    l.pack(padx=50,pady=100)
def no():
    l=[]
    m=[]
    for i in range(550,1200):
        l.append(i)
    for j in range(250,550):
        m.append(j)    
    x1=rc.choice(l)
    y1=rc.choice(m)
    bt1.place(x=x1,y=y1)    
bt=Button(r, text="YES",bg="white",fg="black",font=("italic",30),command=yes)
bt.place(x=300,y=400)
bt1=Button(r, text="NO",bg="white",fg="black",font=("italic",30),command=no)
bt1.place(x=900,y=400)
r.mainloop()