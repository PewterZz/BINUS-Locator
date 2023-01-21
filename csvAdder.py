#Reference: https://www.youtube.com/watch?v=R8NFuQxJ0nk
#Import libraries
from tkinter import *
from tkinter import ttk
import csv

#Set window properties
import pandas as pd

win = Tk()
win.title("Coordinates Adder")
win.geometry('720x1080')

filePath = "coords23.csv"





#Set label texts
Label(win,text='ADD NEW COORDINATES').grid(row=1,column=1,columnspan=2)
Label(win,text='loc').grid(row=2,column=1,columnspan=1)
Label(win,text='type').grid(row=3,column=1,columnspan=1)
Label(win,text='dest').grid(row=4,column=1,columnspan=1)
Label(win,text='dist').grid(row=5,column=1,columnspan=1)
Label(win,text='chain').grid(row=6,column=1,columnspan=1)
#Declare variables
locVar = StringVar()
typeVar = StringVar()
destVar = StringVar()
distVar = StringVar()
chainVar = StringVar()
#Functions
def write():
    df = pd.read_csv(filePath)
    nextRowId = len(df)
    with open (filePath,"a+",newline="") as fobj:

        wt = csv.writer(fobj,delimiter=",")

        id = nextRowId
        loc = locVar.get()
        type = typeVar.get()
        dest = destVar.get()
        dist = distVar.get()
        chain = chainVar.get()

        wt.writerow([id,loc,type,dest,dist,chain])
        print("New coordinate added")
    fobj.close()
#Create input fields and combo boxes
Entry(win,textvariable=locVar).grid(row=2,column=2)

locationCombo= ttk.Combobox(win,width=20,textvariable=typeVar)
locationCombo['values'] = ['street','restaurant','university','recreational','mall']
locationCombo['state'] = 'readonly'
locationCombo.current(0)
locationCombo.grid(row=3,column=2)

Entry(win,textvariable=destVar).grid(row=4,column=2)
Entry(win,textvariable=distVar).grid(row=5,column=2)
Entry(win,textvariable=chainVar).grid(row=6,column=2)


Button(win,text='Add New Coordinate',command=write).grid(row=7,column=1,columnspan=2)


#Run the window
win.mainloop()