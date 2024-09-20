isim="Halef Yurtkuran"
ilk=isim[0]
son=isim[-1]
adet=len(isim)

print(adet) #isim değişkeninin kaç tane eleman içerdiği ekrana yazdırır.--->> 15
print(isim[0:6]) #isim değişkeninin 0'dan 6. karaktere kadar olan kısmını ekrana yazdırır. altıncı karakteri almaz--->> Halef
print(isim[6:])  #6. karakterden başlayarak sona kadar yazdırır-->> Yurtkuran
print(isim[:6])  #[0:6]  ile aynı işlemi yapar ve altıncı karaktere kadar yazdırır.--->> Halef
print(isim[-10:-3]) # yurtku yazısı yazdırılır

print(isim[0:10:2]) #Sıfırdan Onuncu karaktere kadar ikişer ikişer atlayarak yazdır.--->> HlfYr
print(isim[::3])  #Hepsini üçer üçer atlayarak yazdır. --->>HeYtr
print(isim[::-1]) #Tersten Yazdır--->> naruktruY felaH