from tkinter import *

from tkinter.ttk import *

from PIL import Image,ImageTk

from wordlist import *

import random


Window = Tk()

Window.size()

Window.title('Hangman')

Window.geometry("750x400")
#configure the grid
Window.columnconfigure(0, weight=2)
Window.columnconfigure(1, weight=2)

#create frame for image
frame = Frame(Window, width=600, height=400)
frame.grid(column=1,row=0)



#hangman pictures
hangmanbase = ImageTk.PhotoImage(Image.open("hangmanbase.jpg"))
hangman0 = ImageTk.PhotoImage(Image.open("hangman0.jpg"))
hangman1 = ImageTk.PhotoImage(Image.open("hangman1.jpg"))
hangman2 = ImageTk.PhotoImage(Image.open("hangman2.jpg"))
hangman3 = ImageTk.PhotoImage(Image.open("hangman3.jpg"))
hangman4 = ImageTk.PhotoImage(Image.open("hangman4.jpg"))
hangman5 = ImageTk.PhotoImage(Image.open("hangman5.jpg"))

title = Label(Window,text = "Welcome to hangman!").grid(column=0,row=0,sticky='N')

count = 0
startbtn = Button(Window,text="Click To Start",command=lambda:startgame()).grid(column=0,row=0,sticky='N',pady=50)
clsbtn = Button(Window, text = "Click To Close Game",command = Window.destroy).grid(column=0,row=0,pady=25,stick = 'N')



def submit(my_text_box):
    submitch = Button(Window, text = "Submit",command =lambda: getInput(my_text_box))
    submitch.grid(column=0,row=0,sticky='N',pady=50)

def startgame():
    textbox()
    generateword()
    label = Label(frame,image = hangmanbase).pack()

def generateword():
    word = []
    rndmword = random.choice(words)
    for chrcnt in rndmword:
        word.append("_")
    wordlabel = Label(Window, text = word, font = ("Ariel",25)).grid(column=0,row=0,pady=150,sticky = 'N')


def getInput(my_text_box):
    inpt = my_text_box.get("1.0","end-1c")
    #what to do with inpt after submitting, can add functions here
    checkanswer(inpt)

def textbox():    
    my_text_box = Text(Window,height=5, width = 10)
    my_text_box.grid(column=0,row=0,sticky='N',pady=75)
    submit(my_text_box)
    return my_text_box

def checkanswer(inpt):
    print('answer being checked')   

def setimage(count,label):
    if count == 1:
        label = Label(frame,image = hangman0).pack()
    elif count == 2:
        label = Label(frame,image = hangman1).pack()
    elif count == 3:
        label = Label(frame,image = hangman2).pack()
    elif count == 4:
        label = Label(frame,image = hangman3).pack()
    elif count == 5:
        label = Label(frame,image = hangman4).pack()
    elif count == 5:
        label = Label(frame,image = hangman5).pack()


mainloop()