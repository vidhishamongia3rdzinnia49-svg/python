from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()
window.title("Photo Album")
window.geometry("400x420")

title = Label(window, text="My Photo Album", fg="white", bg="purple", width=40)
title.pack(pady=10)

image_file = Image.open("munai.jpeg")
image_file = image_file.resize((300, 180))
photo = ImageTk.PhotoImage(image_file)

pic = Label(window, image=photo)
pic.pack(pady=5)


def show_message():
    messagebox.showinfo("Great", "You clicked the photo")


msg_btn = Button(
    window, text="click to react", bg="blue", fg="white", command=show_message
)
msg_btn.pack(pady=5)


def Show_details():
    top = Toplevel()
    top.title("Photo Details")
    top.geometry("200x120")

    info = Label(top, text="Taken on 1 June 2025")
    info.pack(pady=10)

    location = Label(top, text="Location: My Garden")
    location.pack(pady=10)


details_btn = Button(
    window, text="see details", bg="blue", fg="white", command=Show_details
)
details_btn.pack(pady=5)

window.mainloop()
