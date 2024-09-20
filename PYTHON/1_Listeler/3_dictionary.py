#Dictionary(sözlük)
plakalar={
    "istanbul":34,
    "hatay":31,
    "adana":1,
    "ankara":6
}

print(plakalar["hatay"])

#Kayıt ekleme:
plakalar["izmir"]=36 #plakalar sözlüğüne izmir eklendi.

print(plakalar["izmir"])



#ogrenciler isminde bir sözlük oluşturdum.
ogrenciler={
    #sözlük içerisinde numarasına göre iki tane öğrenci ekledim(küçük sözlük gibi)
    101:{
    "isim":"halef",
    "yas":23,
    "not":80
},

    102:{
    "isim":"ömer",
    "yas":22,
    "not":90
}
}

ogrenci_no=int(input("Öğrenci No:")) #öğrencinin numarasını dışardan giriyoruz.
ogrenci=ogrenciler[ogrenci_no] #sözlükten kullanıcının girdiği öğrenci numarasına ait öğrencinin bilgilerini çekiyoruz.
print(ogrenci["isim"]) # bilgilerini aldığımız öğrencinin ismini yazdırıyoruz.