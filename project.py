import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow kütüphanesi

ekran1 = tk()
ekran1.title("Sport coaching app")
ekran1.geometry("400c800")
ekran1.resizable(False, False)


img = PhotoImage(file = "images\photo1.jpg")
img_label = Label(ekran1, image=img)
img_label.place(x=-45, y=-150)

ekran1.mainloop()
