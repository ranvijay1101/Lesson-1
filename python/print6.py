from tkinteer import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title('Denomination counter')
root.configuration(bg='lightblue')
root.geometry('650x400')
upload = Image.open('image.png')
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
Label = Label(root, image=image, bg='lightblue')
Label.place(x=180, y=20)
Label1 = Label(root,
               text = "hey User! Welcome to Denomination Counter Application.",
               bg = 'lightblue')
Label1.place(relx=0.5, rely=0.1, anchor=CENTER)
def msg():
    MsgBox = messagebox.showinfo(
        "Alert, " "Do you want to caalculate the denomination count?")
    if MsgBox == 'ok':
        topwin()
button1 = Button(root, 
                 text = "Let's get started!",
                 command = msg,
                 bg = 'red'
                 fg = 'white',)
button1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title('Denomination Counter')
    top.geometry('650x400')
    top.configure(bg='lightblue')
    Label2 = Label(top,
                   text = "Enter the amount to calculate the denomination count.",
                   bg = 'lightblue')
label = Label(top, text = "Enter the amount:", bg = 'light grey')
entry = Entry(top)
lbl = Label(top, text="Here are number of notes for each denomination:", bg = 'light grey')
li = Labell(top, text = "2000: ", bg = 'light grey')
l2 = Label(top, text = "500: ", bg = 'light grey')
l3 = Label(top, text = "200: ", bg = 'light grey')
t1 Entry(top)
t2 = Entry(top)
t3 = Entry(top)
def calculator():
    try:
        global amount
        amount = int(entry.get())
        note2000 = amount // 2000
        amount = amount % 2000
        note500 = amount // 500
        amount = amount % 500
        note100 = amount // 100
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer amount.")
        btn = Button(top, text = "Calculate", command = calculator, bg = 'red', fg = 'white')
        label.place(x=230, y=50)
        entry.place(x=200, y=80)
        btn.place(x=240, y=120)
        lbl.place(x=200, y=160)
        li.place(x=200, y=190)
        l2.place(x=200, y=220)
        l3.place(x=200, y=250)
        t1.place(x=300, y=190)
        t2.place(x=300, y=220)
        t3.place(x=300, y=250)
        top.mainloop()
root.mainloop()

