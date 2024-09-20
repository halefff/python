#  Soru1: 'title' değişkeni içerisindeki Karakter Sayısı Nedir?
title = "Python ile Programlama"
print(len(title))

#  Soru2: 'title' içerisindeki 'python' Kelimesini alın
print(title[0:7])

#  Soru3: 'title' değişkeninin ilk 5 ve son 5 karakterini alın.
ilk5=title[0:5]
son5=title[-6:]
print(ilk5 +" "+ son5)

#  Soru4: 'title' değişkenini tersten yazdır.
print(title[::-1])

#Soru5: Klavyeden Girilen Bilgilere Göre Cümle Yazdır.

isim=input("İsminiz")
v=input("Vize:")
f=input("Final:")
o=(float(v)+float(f))/2
sonuc=f"Sayın {isim}, ilk Vize Sonucunuz:{v}, Final Sonucunuz:{f}, Ortalamanız İse:{o} Olarak Hesaplanmıştır"
print(sonuc)