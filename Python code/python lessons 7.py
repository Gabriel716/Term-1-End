#Gabriel Harrison
#9/25


#age=int(input("How old are you?))
#if age > 50:
    #print("You are old")
#else:
    #print("You need to grow up a bit")
from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import calendar
import datetime

def current_time():
    seconds= calendar.timegm(time.gmtime())
    current_seconds=seconds%60
    minutes=seconds//60
    current_minutes=minutes%60
    hours=minutes//60
    current_hour=hours%24
    if current_hour >= 12:
        tag="AM"
    else:
        tag="PM"
    #set the time zone
    current_hour=current_hour -6
    #format the output
    timex=str(current_hour)+":" + str(current_minutes)+":"+str(current_seconds)+tag
    #xreturn the output
    return timex
def quit(*args):
    root.destroy()
def show_time():
    time=current_time()
    #show the time
    txt.set(time)
    #trigger the tick after 1000ms
    root.after(1000,show_time)

#alarm clock
def alarm():
    if time== "9:24:25AM":
        print("Alarm is up")


#use tkinter lib for showing the clock
root=Tk()
root.attributes("-fullscreen", False)
root.configure(background='Black')
root.bind("x",quit)
root.after(1000, show_time)

fnt=font.Font(family='Helvetic', size=60, weight='bold')
txt=StringVar()
lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="Yellow", background="red")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
          
    
    
            
