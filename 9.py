
from ast import Assign
from tkinter import *
import random
window=Tk()
window.title("Program9")
window.geometry("300x200")
errmsg = StringVar()
l1 = Label(window,text="Program 9 tkinter")
l1.grid(row=0)
l2 = Label(window,text="Student Nuber")
l2.grid(row=1,column=0)
student = Entry(window,width=25)
student.grid(row=1,column=1)
l3 = Label(window,text="Program nuber")
l3.grid(row=2,column=0)
program = Entry(window,width=25)
program.grid(row=2,column=1)
def randAssign():
    studentNo = student.get()
    programNo = program.get()
    detail =" "
    if studentNo.isnumeric() and programNo.isnumeric():
        studentNo = int(studentNo)
        programNo = int(programNo)
        for s in range(1,studentNo+1):
            detail+="Student : "+str(s)+ "Program : "+str(random.randint(1,programNo+1))+"\n"
        print(detail)
        file = open("program.csv","w")
        file.write(detail)
        file.close()
        errmsg.set("csv file created")
    else:
        errmsg.set("Invalid input")
Assign = Button(window,width=25,text="Assign",command=randAssign)
Assign.grid(row=3,column=0)
msg = Label(window,textvariable=errmsg)
msg.grid(row=4,column=0)
window.mainloop()
