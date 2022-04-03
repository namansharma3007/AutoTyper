import re
from pynput.keyboard import Controller
from tkinter import *
import tkinter as tk
import time
import keyboard as kb
import webbrowser

root = Tk()
#Windows Title
root.title("AutoTyper")
root.geometry("600x400")
root.resizable(0,0)


keyboard = Controller()

fontSmall= ('', 8)
cursor="hand2"

def callback(event):
    webbrowser.open_new_tab(event)

def rTime():
    time.sleep(4)
def rTime1():
    time.sleep(1)

def linebyline():
    input1=re.sub(r'\t', '', entry.get(1.0, tk.END+"-1c"))
    rTime()
    keyboard.type(input1)

def singleline():
    input1=re.sub(r'\n', '', entry.get(1.0, tk.END+"-1c"))
    rTime()
    keyboard.type(input1)

def linebyline1():
    input1=re.sub(r'\t', '', entry.get(1.0, tk.END+"-1c"))
    rTime1()
    keyboard.type(input1)

def singleline2():
    input1=re.sub(r'\n', '', entry.get(1.0, tk.END+"-1c"))
    rTime1()
    keyboard.type(input1)


entry = tk.Text(root, width=70, height=5)
entry.pack(ipady=70, pady=(10,20))

button1 = tk.Button(root, text="Single Line", command=singleline, foreground="black", font="Helvetica 12", width=10, cursor=cursor)
button1.pack(side=tk.TOP)

kb.add_hotkey('ctrl+7', singleline2)

button2 = tk.Button(root, text="Line By Line", command=linebyline, foreground="black", font="Helvetica 12", width=10, cursor=cursor)
button2.pack(side=tk.TOP,pady=(10,20))

kb.add_hotkey('ctrl+8', linebyline1)


root.attributes('-topmost', True)

root.mainloop()