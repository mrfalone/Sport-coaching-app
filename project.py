import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # Pillow kütüphanesi

ekran1 = Tk()
ekran1.title("Sport coaching app")
ekran1.geometry("400x800")
ekran1.resizable(False, False)

ekran1 = Tk()
ekran1.title("Sport coaching app")
ekran1.geometry("400x800")
ekran1.resizable(False, False)

ekran2 = Tk()
ekran2.title("Sport coaching app")
ekran2.geometry("400x800")
ekran2.resizable(False, False)

ekran3 = Tk()
ekran3.title("Sport coaching app")
ekran3.geometry("400x800")
ekran3.resizable(False, False)

ekran4 = Tk()
ekran4.title("Sport coaching app")
ekran4.geometry("400x800")
ekran4.resizable(False, False)

ekran5 = Tk()
ekran5.title("Sport coaching app")
ekran5.geometry("400x800")
ekran5.resizable(False, False)

img = PhotoImage("photo1.jpg")
img_label = Label(ekran1, image=img)
img_label.place(x=-100, y=300)

img2 = PhotoImage("photo2.jpg")
img_label = Label(ekran1, image=img2)
img_label.place(x=-100, y=300)

img3 = PhotoImage("photo3.jpg")
img_label = Label(ekran1, image=img3)
img_label.place(x=-100, y=300)

img4 = PhotoImage("photo4.jpg")
img_label = Label(ekran1, image=img4)
img_label.place(x=-100, y=300)

img5 = PhotoImage("photo5.jpg")
img_label = Label(ekran1, image=img5)
img_label.place(x=-100, y=300)







ekran1.mainloop()
