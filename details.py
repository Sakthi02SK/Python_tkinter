from tkinter import *
from tkinter import messagebox
s=Tk()
s.geometry("1366x768")
s.config(bg="lightblue")
l=Label(s,text="Information",bg="lightblue",fg="black",font=("Little Bunny",60))
l.place(x=490,y=50)
l1=Label(s,text="Name :",fg="black",bg="lightblue",font=("Easter Park",17))
l1.place(x=240,y=200)
e=Entry(s,fg="blue",font=("Fixedsys",10))
e.place(x=350,y=215)
l2=Label(s,text="Last name :",fg="black",bg="lightblue",font=("Easter Park",17))
l2.place(x=750,y=200)
e1=Entry(s,fg="blue",font=("Fixedsys",10))
e1.place(x=920,y=215)
l3=Label(s,text="Email :",fg="black",bg="lightblue",font=("Easter Park",17))
l3.place(x=240,y=280)
e2=Entry(s,fg="blue",font=("Fixedsys",10))
e2.place(x=350,y=295)
l4=Label(s,text="Reg no :",fg="black",bg="lightblue",font=("Easter Park",17))
l4.place(x=750,y=280)
e3=Entry(s,fg="blue",font=("Fixedsys",10))
e3.place(x=875,y=295)
l5=Label(s,text="Mobile no :",fg="black",bg="lightblue",font=("Easter Park",17))
l5.place(x=240,y=370)
e4=Entry(s,fg="blue",font=("Fixedsys",10))
e4.place(x=370,y=385)
l6=Label(s,text="User name :",fg="black",bg="lightblue",font=("Easter Park",17))
l6.place(x=750,y=370)
e5=Entry(s,fg="blue",font=("Fixedsys",10))
e5.place(x=900,y=385)
l7=Label(s,text="New password :",fg="black",bg="lightblue",font=("Easter Park",17))
l7.place(x=240,y=460)
e6=Entry(s,fg="white",font=("Fixedsys",10))
e6.place(x=420,y=475)
l8=Label(s,text="Confirm password :",fg="black",bg="lightblue",font=("Easter Park",17))
l8.place(x=750,y=460)
e7=Entry(s,fg="white",font=("Fixedsys",10))
e7.place(x=960,y=475)
def submit():
    if len(e4.get())!=10:
        lm=Label(s,text="Check the number",bg="lightblue",fg="red",font=("Arial",9))
        lm.place(x=390,y=405)
    if len(e6.get())<8:
        messagebox.showerror("System","Password must contain 8 characters")
    else:
        if e6.get()!=e7.get():
            l10=Label(s,text="Re enter ur password",bg="lightblue",fg="red",font=("Arial",9))
            l10.place(x=970,y=495)
        else:
            a=Tk()
            a.geometry("1366x768")
            a.config(bg="lightblue")
            l=Label(a,text="Details",fg="black",bg="lightblue",font=("Jost_Futuristic_Style",70))
            l.place(x=560,y=50)
            l1=Label(a,text="Name :",fg="black",bg="lightblue",font=("Easter Park",17))
            l1.place(x=450,y=200)
            l2=Label(a,text="Email :",fg="black",bg="lightblue",font=("Easter Park",17))
            l2.place(x=450,y=280)
            l3=Label(a,text="Reg no :",fg="black",bg="lightblue",font=("Easter Park",17))
            l3.place(x=450,y=360)
            l4=Label(a,text="Mobile no :",fg="black",bg="lightblue",font=("Easter Park",17))
            l4.place(x=450,y=440)
            l5=Label(a,text="{0} {1}".format(e.get(),e1.get()),fg="blue",bg="lightblue",font=("Hamer",17))
            l5.place(x=530,y=207)
            l6=Label(a,text="{}".format(e2.get()),fg="blue",bg="lightblue",font=("Hamer",17))
            l6.place(x=530,y=290)
            l7=Label(a,text="{}".format(e3.get()),fg="blue",bg="lightblue",font=("Hamer",17))
            l7.place(x=530,y=370)
            l8=Label(a,text="{}".format(e4.get()),fg="blue",bg="lightblue",font=("Hamer",17))
            l8.place(x=560,y=445)
            def confirm():
                s.destroy()
                messagebox.showinfo("SK","Completed")
            b=Button(a,text="Confirm",font=("Script",15),command=confirm)
            b.place(x=600,y=550)
b=Button(s,text="Submit",font=("28 Days Later",15),width=8,height=1,command=submit)
b.place(x=600,y=560)
s.mainloop()