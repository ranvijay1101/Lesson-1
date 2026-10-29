from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.title('My Photo album')
window.geometry('400x420')
title = Label(window, text='My Photo Album', fg='white', bg='purple', width=40)
title.pack(pady=10)
img_file = Image.open('myphoto.jpeg')
img_file = img_file.resize((300, 300))
photo = ImageTk.PhotoImage(img_file)
photo_label = Label(window, image=photo)
photo_label.pack(pady=10)
def show_message():
    messagebox.showinfo('Great!', 'You clicked a photo!') 
msg_btn = Button(window, text='Click Me!', bg='purple', fg='white', width=20, command=show_message)
msg_btn.pack(pady=5)
def show_details():
    top =  Toplevel()
    top.title('Photo Details')
    top.geometry('300x200')
    info = Label(top, text= 'Taken on 11th september 2001')
    info.pack(pady=10)
    place = Label(top, text= 'Place: New York')
    place.pack()
    top.mainloop()
details_btn = Button(window, text='Show Details', bg='purple', fg='white', width=20, command=show_details)
details_btn.pack(pady=5)
window.mainloop()