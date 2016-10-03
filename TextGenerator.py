import random,string,Tkinter
from Tkinter import *

window = Tk()

def generator():
    n = int(e1Value.get())
    s = float(e2Value.get())
    i = 0
    textList = []
    text = ''
    while i<n:
        randomSpaceIndex = random.random()
        if randomSpaceIndex >= s:
            textList.insert(i,random.choice(string.ascii_letters))
            text = text + textList[i]
            i = i + 1
        else:
            text = text + ' '

    t1.insert(END,text)


l1 = Label(window,text='Number of characters')
l1.grid(row=0,column=0)

l2 = Label(window,text='Frequency [0,1) of spaces')
l2.grid(row=3,column=0)


e1Value = StringVar()
e1 = Entry(window,textvariable=e1Value)
e1.grid(row=0,column=1)


e2Value = StringVar()
e2 = Entry(window,textvariable=e2Value)
e2.grid(row=3,column=1)


b1 = Button(window,text = "Generate",command=generator)
b1.grid(row=5,column=1)

t1 = Text(window,height=60,width=30)
t1.grid(row=7,column=0)

window.mainloop()
