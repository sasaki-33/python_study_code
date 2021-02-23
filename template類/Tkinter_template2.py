#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import tkinter
import random
import time
from PIL import Image, ImageTk
import urllib.request as req
b = 1500
root = tkinter.Tk()
root.title(u'ボタンを押して始まります。')
root.geometry('800x450')

def f(event):
    entry1.delete(0,tkinter.END)
    entry1.insert(tkinter.END,'00000')
    global b
    b = 1500

def i(event):
    entry.delete(0,tkinter.END)
    w = random.randint(1,48)
    if w <=25:
        list = [333,777]
        s = random.choice(list)
        entry.insert(tkinter.END,'{}'.format(s))
        global b
        entry1.delete(0,tkinter.END)
        entry1.insert(tkinter.END,'{}'.format(b))
        b += 1500
        
        
    else:
        sa = random.randint(111,999)
        if sa == 111 or 222 or 333 or 444 or 555 or 666 or 777 or 888 or 999:
            ha = random.randint(1,9)
            entry.insert(tkinter.END,'{}'.format(sa+ha))
        else:
            entry.insert(tkinter.END,'{}'.format(sa))
    

entry = tkinter.Entry(width = 3,font =( '',80))
entry.insert(tkinter.END,'000')
entry.pack()

entry1 = tkinter.Entry(width = 5,font = ('',40))
entry1.insert(tkinter.END,'00000')
entry1.pack()

button1 = tkinter.Button(text = u'delete')
button1.pack()
button1.bind('<Button-1>',f)

button = tkinter.Button(text = u'start')
button.pack()
button.bind('<Button-1>',i)

root.mainloop()