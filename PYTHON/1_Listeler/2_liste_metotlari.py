sayilar = [2,5,13,2,6,43,976,54,3,2,38,2]
isimler=["Ömer", "Zehra", "Medine", "Büşra", "Enes", "Perihan", "Hüseyin"]

sonuc=min(sayilar) #en küçük sayıyı yazdırır.
sonuc2=min(isimler) #alfabetik sıraya göre yazdırır. max metodu tam tersini yazdırır.
print(sonuc,sonuc2)


#Ekleme İşlemi:
sayilar.append(25) #en sona 25 sayısını ekler
isimler.append("Halef")
print(sayilar,isimler)

sayilar.insert(0,15) #sıfırıncı indexe 15 sayısını ekler
print(sayilar)


#Silme İşlemleri:
sayilar.pop() #listenin son sayısını siler
sayilar.pop(3) #üçüncü index nmarasına ait sayıyı siler
print(sayilar)

isimler.remove("Halef") #isimler listesinden halef ismini siler.
print(isimler)

sayilar.sort() #sayilari küçükten büyüğe doğru sırala.
isimler.sort() #isimleri alfabetik sırala
print(sayilar,isimler)

sayilar.reverse() #sayıları büyükten küçüğe sıralar.
print(sayilar)


sonuc3 = sayilar.count(2) #sayıların içinde kaç tane 2 var?
print(sonuc3)