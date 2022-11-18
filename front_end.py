from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font


def jalandhar():
    root = Tk()
    root.geometry('500x500')
    labe = Label(root, text="JALANDHAR", font=(
        "Helvitika", 20, 'bold'), bg='grey').place(x=180, y=10)
    labe1 = Label(root, text="1 . JALANDHAR : 0 Kilo Meters").place(
        x=160, y=65)
    labe1 = Label(root, text="2 . LUDHIANA : 61 Kilo Meters").place(
        x=160, y=95)
    labe1 = Label(root, text="3 . AMRITSAR : 80 Kilo Meters").place(
        x=160, y=125)
    labe1 = Label(root, text="4 . CHANDIGARH : 149 Kilo Meters").place(
        x=160, y=155)
    labe1 = Label(root, text="5 . PATIALA : 154 Kilo Meters").place(
        x=160, y=185)


def amrister():
    root = Tk()
    root.geometry('500x500')
    labe = Label(root, text="Amrister", font=(
        "Helvitika", 20, 'bold'), bg='grey').place(x=180, y=10)
    labe1 = Label(root, text="1 . AMRITSAR : 0 Kilo Meters").place(x=160, y=65)
    labe1 = Label(root, text="2 . JALANDHAR : 80 Kilo Meters").place(
        x=160, y=95)
    labe1 = Label(root, text="3 . LUDHIANA : 140 Kilo Meters").place(
        x=160, y=125)
    labe1 = Label(root, text="4 . CHANDIGARH : 229 Kilo Meters").place(
        x=160, y=155)
    labe1 = Label(root, text="5 . PATIALA : 235 Kilo Meters").place(
        x=160, y=185)


def ludhina():
    root = Tk()
    root.geometry('500x500')
    labe = Label(root, text="LUDHINA", font=(
        "Helvitika", 20, 'bold'), bg='grey').place(x=180, y=10)
    labe1 = Label(root, text="1 . LUDHIANA : 0 Kilo Meters").place(x=160, y=65)
    labe1 = Label(root, text="2 . JALANDHAR : 61 Kilo Meters").place(
        x=160, y=95)
    labe1 = Label(root, text="3 . PATIALA : 93 Kilo Meters").place(
        x=160, y=125)
    labe1 = Label(root, text="4 . CHANDIGARH : 106 Kilo Meters").place(
        x=160, y=155)
    labe1 = Label(root, text="5 . AMRITSAR : 140 Kilo Meters").place(
        x=160, y=185)


def chandigharh():
    root = Tk()
    root.geometry('500x500')
    labe = Label(root, text="CHANDIGHARH", font=(
        "Helvitika", 20, 'bold'), bg='grey').place(x=180, y=10)
    labe1 = Label(root, text="1 . CHANDIGARH : 0 Kilo Meters").place(
        x=160, y=65)
    labe1 = Label(root, text="2 . PATIALA : 75 Kilo Meters").place(x=160, y=95)
    labe1 = Label(root, text="3 . LUDHIANA : 106 Kilo Meters").place(
        x=160, y=125)
    labe1 = Label(root, text="4 . JALANDHAR : 149 Kilo Meters").place(
        x=160, y=155)
    labe1 = Label(root, text="5 . AMRITSAR : 229 Kilo Meters").place(
        x=160, y=185)


def patiala():
    root = Tk()
    root.geometry('500x500')
    labe = Label(root, text="PATIALA", font=(
        "Helvitika", 20, 'bold'), bg='grey').place(x=180, y=10)
    labe1 = Label(root, text="1 . PATIALA : 0 Kilo Meters").place(x=160, y=65)
    labe1 = Label(root, text="2 . CHANDIGARH : 75 Kilo Meters").place(
        x=160, y=95)
    labe1 = Label(root, text="3 . LUDHIANA : 93 Kilo Meters").place(
        x=160, y=125)
    labe1 = Label(root, text="4 . CHANDIGARH : 149 Kilo Meters").place(
        x=160, y=155)
    labe1 = Label(root, text="5 . AMRITSAR : 235 Kilo Meters").place(
        x=160, y=185)


frame = Tk()
# frame=Frame(frame)
frame.geometry('800x500')
frame.title("Travelling salesman problem")
frame.config(bg='white')
frame.maxsize(800, 550)
frame.minsize(800, 550)
img = Image.open("C:\\Users\\nbhar\\Documents\\Documents\\Desktop\\py_project\\Map.png")
img = img.resize((500, 300))
pic = ImageTk.PhotoImage(img)
v1 = Label(image=pic)
v1.place(x=100, y=50)
# v1.place(x=100,y=35)
# lavle=Label(frame,text="Travelling salesman problem",font="")
# lavle.place(x=350,y=10)

boo = Label(frame, text="Travelling Salesman problem", bg="white",
            font=("Helvitika", 20, 'bold')).place(x=185, y=10)

op = Label(frame, text="CHOOSE YOUR CITY TO GET THE SHORTEST DISTANCE",
           font=("Helvitika", 10, 'bold')).place(x=180, y=400)
jil_jil = Button(frame, text="About the Developers", foreground="white",
                 width=25, bg="black", font=("Helvitika", 13, 'bold')).place(x=250, y=520)
but = Button(frame, text="Amrister", command=amrister,
             bg='grey').place(x=100, y=450)
but = Button(frame, text="Jalandhar", command=jalandhar,
             bg='grey').place(x=220, y=450)
but = Button(frame, text="Ludhina", command=ludhina,
             bg='grey').place(x=320, y=450)
but = Button(frame, text="Chandigarh", command=chandigharh,
             bg='grey').place(x=420, y=450)
but = Button(frame, text="Patiala", command=patiala,
             bg='grey').place(x=540, y=450)
frame.mainloop()
