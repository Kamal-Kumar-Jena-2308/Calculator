from tkinter import *
from PIL import Image, ImageTk
import os
tk=Tk()
tk.title('Calculator - By Kamal Kumar Jena')
tk.geometry('500x605')
tk.resizable(False,False)
a=StringVar()
img=Image.open('img.jpg')
img=img.resize((100,100), Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)
def b1c():
    screen.configure(state=NORMAL)
    b=a.get()
    screen.insert((len(b)), "1")
    screen.configure(state=DISABLED)
def b2c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "2")
    screen.configure(state=DISABLED)
def b3c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "3")
    screen.configure(state=DISABLED)
def b4c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "4")
    screen.configure(state=DISABLED)
def b5c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "5")
    screen.configure(state=DISABLED)
def b6c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "6")
    screen.configure(state=DISABLED)
def b7c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "7")
    screen.configure(state=DISABLED)
def b8c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "8")
    screen.configure(state=DISABLED)
def b9c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "9")
    screen.configure(state=DISABLED)
def b0c():
    b=a.get()
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "0")
    screen.configure(state=DISABLED)
def bac():
    b=a.get()
    if b[len(b)-1] == "=" or b[len(b)-1] == "÷" or b[len(b)-1] == "×" or b[len(b)-1] == "-" or b[len(b)-1] == "+":
        return 0
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "+")
    screen.configure(state=DISABLED)
def bsc():
    b=a.get()
    if b[len(b)-1] == "=" or b[len(b)-1] == "÷" or b[len(b)-1] == "×" or b[len(b)-1] == "-" or b[len(b)-1] == "+":
        return 0
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "-")
    screen.configure(state=DISABLED)
def bmc():
    b=a.get()
    if b[len(b)-1] == "=" or b[len(b)-1] == "÷" or b[len(b)-1] == "×" or b[len(b)-1] == "-" or b[len(b)-1] == "+":
        return 0
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "×")
    screen.configure(state=DISABLED)
def bdc():
    b=a.get()
    if b[len(b)-1] == "=" or b[len(b)-1] == "÷" or b[len(b)-1] == "×" or b[len(b)-1] == "-" or b[len(b)-1] == "+":
        return 0
    screen.configure(state=NORMAL)
    screen.insert((len(b)), "÷")
    screen.configure(state=DISABLED)
def bgc():
    b=a.get()
    b=b.replace("÷","/")
    b=b.replace("×","*")
    try:
        result=eval(b)
        a.set(int(result))
        screen.configure(state=DISABLED)
    except:
        return 0
def brc():
    b=a.get()
    if b=="":
        return 0
    screen.configure(state=NORMAL)
    screen.delete(len(b)-1,END)
    screen.configure(state=DISABLED)

b1=Button(text="1",font="Impact 50 bold",command=b1c)
b1.place_configure(x=20,y=160,height=100,width=100)
b2=Button(text="2",font="Impact 50 bold", command=b2c)
b2.place_configure(x=140,y=160,height=100,width=100)
b3=Button(text="3",font="Impact 50 bold",command=b3c)
b3.place_configure(x=260,y=160,height=100,width=100)
b4=Button(text="4",font="Impact 50 bold",command=b4c)
b4.place_configure(x=20,y=270,height=100,width=100)
b5=Button(text="5",font="Impact 50 bold",command=b5c)
b5.place_configure(x=140,y=270,height=100,width=100)
b6=Button(text="6",font="Impact 50 bold",command=b6c)
b6.place_configure(x=260,y=270,height=100,width=100)
b7=Button(text="7",font="Impact 50 bold",command=b7c)
b7.place_configure(x=20,y=380,height=100,width=100)
b8=Button(text="8",font="Impact 50 bold",command=b8c)
b8.place_configure(x=140,y=380,height=100,width=100)
b9=Button(text="9",font="Impact 50 bold",command=b9c)
b9.place_configure(x=260,y=380,height=100,width=100)
b0=Button(text="0",font="Impact 50 bold",command=b0c)
b0.place_configure(x=140,y=490,height=100,width=100)
badd=Button(text="+",font="Impact 50 bold", command=bac)
badd.place_configure(x=380,y=160,height=100,width=100)
bsub=Button(text="-",font="Impact 50 bold", command=bsc)
bsub.place_configure(x=380,y=270,height=100,width=100)
bmul=Button(text="×",font="Impact 50 bold", command=bmc)
bmul.place_configure(x=380,y=380,height=100,width=100)
bdiv=Button(text="÷",font="Impact 50 bold", command=bdc)
bdiv.place_configure(x=380,y=490,height=100,width=100)
bcal=Button(font="Impact 50 bold", command=bgc,image=img,text="=")
bcal.place_configure(x=270,y=490,height=100,width=100)
bcle=Button(text="CE",font="Impact 45 bold", command=brc)
bcle.place_configure(x=20,y=490,height=100,width=100)
screen=Entry(font="algerian 43", textvariable=a)
screen .place_configure(x=10,y=10,height=100,width=480)
scroller=Scrollbar(tk, orient=HORIZONTAL)
scroller.pack_configure(fill='x', expand=True)
scroller.place(x=5,y=115, width=495)
scroller.config(command=screen.xview)
screen.configure(state=DISABLED, xscrollcommand=scroller.set)
tk.mainloop()