# kullanıcı adı ya da e-mail ile giriş işlemi:
username="halef"
email="deneme@gmail"
sifre="123"

girilen_bilgi=input("Kullanıcı Adı Ya da email: ")
girilen_sifre=input("Şifreniz: ")

giris=( ((girilen_bilgi==username)or(girilen_bilgi==email)) and (girilen_sifre==sifre))
if giris==False:
    print("Giriş Başarısız")
else:
    print("Giriş Başarılı")