from tkinter import *
from tkinter import messagebox
import sqlite3

ekran=Tk()
ekran.title("Sport Center Project")
ekran.geometry("370x600+500+200")
ekran.config(bg = "#8D7160")
ekran_icon = PhotoImage(file=r"images\icon.png")
ekran.iconphoto(False, ekran_icon)


listeKutusu=""
listelePenceresi=""

# ---------------------------------------------------------------------------- #
#                          VERITABANININ OLUŞTURULMASI                         #
# ---------------------------------------------------------------------------- #
# Veritabanı dosyamızın oluşturulması (Bağlantı oluşturulması)

kisiselbilgi=sqlite3.connect("kisiselbilgi.db")
curr=kisiselbilgi.cursor()
# ---------------------------------------------------------------------------- #
# Kitap Kaydı Tablosunun Oluşturulması
#IF NOT EXISTS  ekleyerek defalarca aynı tablos oluşuturulmasını istek yapmıyoruz.Bu da hata almamızı engelliyor
curr.execute(''' CREATE TABLE IF NOT EXISTS kisiselbilgi (
  userID INTEGER PRIMARY KEY,
  isim VARCHAR(50),
  nickname VARCHAR(15),
  sifre INTEGER,
  yas INTEGER
  )   ''')

kisiselbilgi.commit()
kisiselbilgi.close()

# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
def duzenle():
    def guncelleme():
        user=userID.get()
        ad=isim.get()
        name=nickname.get()
        password=sifre.get()
        age=yas.get()
              
        #veritabanı bağlantısını oluşutrduk
        kisiselbilgi=sqlite3.connect("kisiselbilgi.db")
        curr=kisiselbilgi.cursor()
        curr.execute(''' INSERT INTO kisiselbilgi (userID,isim,nickname,sifre,yas) VALUES 
        (?,?,?,?,?)''',(user,ad,name,password,age))
        kisiselbilgi.commit()
        kisiselbilgi.close() 
                
              Listele()   

      guncelleButon=Button(guncellePenceresi,text="GUNCELLE",command=guncelleme)
      guncelleButon.place(x=120,y=120)
      
      
      secilen=listeKutusu.curselection()
      secilmis=secilen[0]
    
      bilgi=listeKutusu.get(secilen)
      print(bilgi[0])
      
      guncellePenceresi=Toplevel(listelePenceresi)
      guncellePenceresi.geometry("250x250")
      guncellePenceresi.title("GÜNCELLE")
      
      Label(guncellePenceresi, text="UserID:").place(x=20, y=10)
      uyeAdi = Entry(guncellePenceresi)
      uyeAdi.place(x=80, y=10)

      Label(guncellePenceresi, text="Isim:").place(x=20, y=40)
      ISBN = Entry(guncellePenceresi)
      ISBN.place(x=80, y=40)

      Label(guncellePenceresi, text="NickName:").place(x=20, y=80)
      AlınısTarihi = Entry(guncellePenceresi)
      AlınısTarihi.place(x=80, y=80)
      
      
      
      
     
      
def sil():
      
      cevap=messagebox.askokcancel("Onay Kutusu","Silmek istediğinize emin misiniz?:")
      
      if cevap:          
          secilen=listeKutusu.curselection()
          secilmis=secilen[0]        
          bilgi=listeKutusu.get(secilen)
          print(bilgi[0])
          #veritabanı bağlantısını oluşutrduk
          kisiselbilgi=sqlite3.connect("kisiselbilgi.db")
          curr=kisiselbilgi.cursor()
          curr.execute(''' DELETE FROM kisiselbilgi WHERE userID=?''',(bilgi[0],)  )
          kisiselbilgi.commit()
          kisiselbilgi.close() 
          Listele()





def Listele():
      global listeKutusu
      global listelePenceresi
      listelePenceresi=Toplevel(ekran)
      listelePenceresi.geometry("350x500+500+300")
      listelePenceresi.title("Listeleme Ekranı")
      
      duzenleButton=Button(listelePenceresi,text="DÜZENLE",command=duzenle)
      duzenleButton.place(x=280,y=50)
      
      silButton=Button(listelePenceresi,text="KAYIT SİL",command=sil)
      silButton.place(x=280,y=90)
      
      
      # Veritabanı bağlantısı
      kisiselbilgi=sqlite3.connect("kisiselbilgi.db")
      curr=kisiselbilgi.cursor()
      # Yapılacak işlemler bu arada yapılıyor. Sadece bu kısım değişiyor
      curr.execute(''' SELECT * FROM  kisiselbilgi''')
      # fetch işlemi bir şeyi al getir anlamında. Burdada verileri çekmek için kullanılır.
      bilgiler=curr.fetchall()
  
      kisiselbilgi.close()
      listeKutusu=Listbox(listelePenceresi,height=20,width=40)
      listeKutusu.place(x=20,y=10)
    
      
      for bilgi in bilgiler:
            
            listeKutusu.insert(END,bilgi)
      







# # Resim Ekleme
# resim = Image.open("images\kitapKurdu.png")  # Resmi aç
# resim = resim.resize((200, 200), Image.ANTIALIAS)  # Resmi boyutlandır
# resim = ImageTk.PhotoImage(resim)  # Resmi Tkinter PhotoImage nesnesine dönüştür
# etiket = Label(ekran, image=resim)  # Etiket oluştur
# etiket.place(x=500, y=30)  # Sağ üst köşeye yerleştir

# ---------------------------------------------------------------------------- #


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


    # YENİ ELEMAN KAYIT İŞLEME
    def Kaydet():
        
        user=userID.get()
        ad=isim.get()
        name=nickname.get()
        password=sifre.get()
        age=yas.get()

        print(user, ad, name, password, age)
        # Veritabanı bağlantısı
        kisiselbilgi=sqlite3.connect("kisiselbilgi.db")
        curr=kisiselbilgi.cursor()
        curr.execute(''' INSERT INTO kisiselbilgi (userID,isim,nickname,sifre,yas) VALUES 
        (?,?,?,?,?)''',(user,ad,name,password,age))
        kisiselbilgi.commit()
        kisiselbilgi.close()

    AdLabel=Label(registerPage,text="PERSONAL SPORT COACHING APP", font = ("Inter 10"))
    AdLabel.place(x=56,y=3)

    # Girişler ve Etiketlers
    Label(registerPage, text="Üye ID:").place(x=100, y=30)
    userID = Entry(registerPage)
    userID.place(x=200, y=30)

    Label(registerPage, text="Isim:").place(x=100, y=60)
    isim = Entry(registerPage)
    isim.place(x=200, y=60)

    Label(registerPage, text="Üye nickname:").place(x=100, y=90)
    nickname = Entry(registerPage)
    nickname.place(x=200, y=90)

    Label(registerPage, text="Yas:").place(x=100, y=120)
    yas = Entry(registerPage)
    yas.place(x=200, y=120)

    Label(registerPage, text="Sifre:").place(x=100, y=150)
    sifre = Entry(registerPage)
    sifre.place(x=200, y=150)
    print("merhaba")

    kaydetButon = Button(registerPage, text="KAYDET", command=Kaydet)
    kaydetButon.place(x=150, y=180) 

    listeleButton=Button(registerPage,text="LİSTELE",command=Listele)
    listeleButton.place(x=210,y=180)

def Login():
    
    loginPage=Toplevel(ekran)
    loginPage.title("Login Page")
    loginPage.geometry("400x600+500+200")
    loginPage.config(bg = "#8D7160")
    loginPage_icon = PhotoImage(file=r"images\icon.png")
    loginPage.iconphoto(False, loginPage_icon)

    AdLabel=Label(loginPage,text="PERSONAL SPORT COACHING APP",font = ("Inter 10"))
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

    AdLabel=Label(personalPage,text="PERSONAL SPORT COACHING APP", fg=("black"),font = ("Inter 10"))
    AdLabel.place(x=56,y=3)








AdLabel=Label(ekran,text=("PERSONAL SPORT COACHING APP"),font = ("Inter 10"))
AdLabel.place(x=56,y=3)

loginButton=Button(ekran,text="Login Page",command=Login)
loginButton.place(x=20,y=36)
 
signupButton=Button(ekran,text="Sign up",command=register)
signupButton.place(x=140,y=36)

personalButton=Button(ekran,text="Personal Information",command=personal)
personalButton.place(x=233,y=36)








ekran.mainloop()