from tkinter import *


ekran=Tk()
ekran.title("Sport Center Project")
ekran.geometry("370x600+500+200")
ekran.config(bg = "#8D7160")
ekran_icon = PhotoImage(file=r"images\icon.png")
ekran.iconphoto(False, ekran_icon)

#img = PhotoImage(file = "D:\python_proje\Sport-coaching-app\images\menu_photo.jpg")
#img_label = Label(ekran, image=img)
#img_label.place(x=-98, y=-9)

def register():
    registerPage=Toplevel(ekran)
    registerPage.title("Register Page")
    registerPage.geometry("400x600+500+200")
    registerPage.config(bg = "#8D7160")
    registerPage_icon = PhotoImage(file=r"images\icon.png")
    registerPage.iconphoto(False, registerPage_icon)

    AdLabel=Label(registerPage,text="PERSONAL SPORT COACHING APP")
    Label.config(font = ("Inter 10"))
    AdLabel.place(x=56,y=3)
    
    AdLabel=Label(registerPage,text="Name:", bg = "#8D7160")
    AdLabel.place(x=45,y=80)
    
    AdLabel=Label(registerPage,text="Mail:", bg = "#8D7160")
    AdLabel.place(x=45,y=100)
    
    AdLabel=Label(registerPage,text="Password:", bg = "#8D7160")
    AdLabel.place(x=45,y=120)

def Login():
    loginPage=Toplevel(ekran)
    loginPage.title("Login Page")
    loginPage.geometry("400x600+500+200")
    loginPage.config(bg = "#8D7160")
    loginPage_icon = PhotoImage(file=r"images\icon.png")
    loginPage.iconphoto(False, loginPage_icon)

    AdLabel=Label(loginPage,text="PERSONAL SPORT COACHING APP")
    Label.config(font = ("Inter 10"))
    AdLabel.place(x=56,y=3)

    AdLabel=Label(loginPage,text="Name:",bg = "#8D7160")
    AdLabel.place(x=100,y=100)

    AdLabel=Label(loginPage,text="Password:",bg = "#8D7160")
    AdLabel.place(x=100,y=125)




def personal():
    personalPage=Toplevel(ekran)
    personalPage.title("Personal Information")
    personalPage.geometry("400x600+500+200")
    personalPage.config(bg = "#8D7160")
    personalPage_icon = PhotoImage(file=r"images\icon.png")
    personalPage.iconphoto(False, personalPage_icon)

    AdLabel=Label(personalPage,text="PERSONAL SPORT COACHING APP")
    Label.config(font = ("Inter 10"))
    AdLabel.place(x=56,y=3)








AdLabel=Label(ekran,text="PERSONAL SPORT COACHING APP")
AdLabel.config(font = ("Inter 10"))
AdLabel.place(x=56,y=3)

loginButton=Button(ekran,text="Login Page",command=Login)
loginButton.place(x=20,y=36)
 
signupButton=Button(ekran,text="Sign up",command=register)
signupButton.place(x=140,y=36)

personalButton=Button(ekran,text="Personal Information",command=personal)
personalButton.place(x=233,y=36)

ekran.mainloop()