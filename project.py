from tkinter import *


ekran=Tk()
ekran.title("Sport Center Project")
ekran.geometry("300x500+500+200")



def register():
    registerPage=Toplevel(ekran)

def Login():
    loginPage=Toplevel(ekran)
    loginPage.title("Login Page")
    loginPage.geometry("400x600+500+200")
    AdLabel=Label(loginPage,text="Adınızı Girin:")
    AdLabel.place(x=100,y=100)
  



loginButton=Button(ekran,text="Login Page",command=Login)
loginButton.place(x=150,y=100)



ekran.mainloop()