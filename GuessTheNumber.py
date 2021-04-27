from tkinter.ttk import *
from tkinter import *
import random
import time

win = Tk()
win.title("Guess The Number")
win.geometry("370x310")

win.configure(background = "#261E36")
number = random.randint(0, 100)
b=0
tryclr = "#00FF22"
tries = 0
diffnum = 100

def Exit():
    win.destroy()

def Random():
    global number,rannum,randig,a,b,tries,diff,diffnum,tryclr
    tryclr = "#00FF22"
    trieslbl.config(fg = tryclr)
    if diff.get()==1:diffnum = 50
    elif diff.get()==2:diffnum = 100
    elif diff.get()==3:diffnum = 200
    randig=""
    rannum = Label(win,fg="#16C1D4",text = randig,bg="#261E36", font=('Helvetica', 20,"bold"))
    rannum.grid(column = 0,row = 5,columnspan = 3)
    number = random.randint(0, diffnum)
    a=0
    tries = 0
    trieslbl.config(text ="Tries:"+ str(tries))
    txt.config(state='normal')
    txt.delete(0, END)
    Piclbl.config(image=die)
    while (a<10):
        b = random.randint(1,5)
        if b ==1:
            rannum.config(text = ".")
            rannum.update()
        elif b ==2:
            rannum.config(text = "..")
            rannum.update()
        elif b ==3:
            rannum.config(text = "...")
            rannum.update()
        elif b ==4:
            rannum.config(text = "....")
            rannum.update()
        elif b ==5:
            rannum.config(text = ".....")
            rannum.update()
        time.sleep(0.2)
        a=a+1
    time.sleep(0.2)
    rannum.config(text = "Your number\nis ready!", font=('Helvetica', 8,"bold"),fg="#16C1D4")
    rannum.update()
    time.sleep(2)
    rannum.config(text="")

def Game(*args):
    global number,txtnum,Piclbl,x,donwarrow,uparrow,correct,txt,tries,trieslbl,tryclr
    txtnum = txt.get()
    if txtnum == str(""):x=0
    else:
        if int(txtnum) > int(number):
            tries = tries + 1
            if tries == 3:tryclr = "#EFFF00"
            elif tries == 6:tryclr = "#FFB300"
            elif tries == 9:tryclr = "#FF0000"
            trieslbl.config(text ="Tries:"+ str(tries),fg = tryclr)
            Piclbl.config(image=downarrow)
        elif int(txtnum) < int(number):
            tries = tries + 1
            if tries == 3:tryclr = "#EFFF00"
            elif tries == 6:tryclr = "#FFB300"
            elif tries == 9:tryclr = "#FF0000"
            trieslbl.config(text ="Tries:"+ str(tries),fg = tryclr)
            Piclbl.config(image=uparrow)
        elif int(txtnum) == int(number):
            tries = tries + 1
            if tries == 3:tryclr = "#EFFF00"
            elif tries == 6:tryclr = "#FFB300"
            elif tries == 9:tryclr = "#FF0000"
            trieslbl.config(text ="Tries:"+ str(tries),fg = tryclr)
            Piclbl.config(image=correct)
            txt.config(state = 'disabled')
    txt.delete(0, END)

uparrow = PhotoImage(file="uparrow.png")
downarrow = PhotoImage(file="downarrow.png")
correct = PhotoImage(file="correct.png")
die = PhotoImage(file="die.png")

titlelbl = Label(win , text="Guess the Number",bg="#261E36", fg="#16C1D4", font=('Helvetica', 20, 'bold'), justify=CENTER, borderwidth=10, relief="groove")
titlelbl.grid(column=0, columnspan=3, row=0)
instructionslbl = Label(bg="#261E36", fg="#16C1D4", font=('Helvetica', 12,"bold"),text="In this Game you will try to find a secret  number"
                                                                                       "\nthat is randomly chosen every round"
                                                                                       "\nTry to guess it with the least possible tries!")

instructionslbl.grid(column=0, columnspan=3, row=2)

diff=IntVar()
diff.set(2)
rad1 = Radiobutton(win, text="Easy(0-50)", value=1,var=diff,bg="#261E36", fg="#16C1D4", font=('Helvetica', 10,"bold"), borderwidth=4, relief="groove")
rad2 = Radiobutton(win, text="Normal(0-100)", value=2,var=diff,bg="#261E36", fg="#16C1D4", font=('Helvetica', 10,"bold"), borderwidth=4, relief="groove")
rad3 = Radiobutton(win, text="Hard(0-200)", value=3,var=diff,bg="#261E36", fg="#16C1D4", font=('Helvetica', 10,"bold"), borderwidth=4, relief="groove")
rad1.grid(column=0,row=1,pady = 10)
rad2.grid(column=1,row=1,pady = 10)
rad3.grid(column=2,row=1,pady = 10)

txt = Entry(win, width=9, font=('Helvetica', 10,"bold"),bg = "#737373",fg = "cyan",justify = CENTER)
txt.grid(column=0, row=3,columnspan = 3)
Piclbl = Label(win, image=die, bg='#261E36')
Piclbl.grid(column=0, row=3,rowspan = 2)
exitbtn = Button(win, text="Exit", command=Exit, width=10, heigh=2,font=('Helvetica', 11, 'bold'),bg="#95D2FF")
exitbtn.grid(column=2, row=3)
restartbtn = Button(win, text="Randomize", command=Random, width=10, heigh=2,font=('Helvetica', 11, 'bold'),bg="#95D2FF")
restartbtn.grid(column=2, row=4)
trieslbl = Label(win, width=9, font=('Helvetica', 9,"bold"),bg ='#261E36',fg = tryclr,justify = CENTER,text = "Tries:"+ str(tries), borderwidth=3, relief="groove",height = 2)
trieslbl.grid(column=0, row=4,columnspan = 3)

win.bind("<Return>",Game)

win.mainloop()