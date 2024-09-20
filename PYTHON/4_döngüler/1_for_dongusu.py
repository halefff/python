sayilar=[1,2,4,3,6,7,34,86,8]
isimler="halef","ömer","zehra"
adsoyad="halef yurtkuran"
mytuple=[(1,2),(3,4),(5,6)]
my_dict={
    "31":"Hatay",
    "34":"İstanbul",
    "06":"Ankara"
}

for i in sayilar: #sayilar listesi içerisindeki her elemanı teker teker alır. aşağıdaki print ifadesiyle alt alta yazdırır.
    print(i)

for x in isimler: #isimler listesindeki her ismi teker teker alır ve print ifadesiyle alt alta yazdırır.
    print(x)

for y in adsoyad: #adsoyad değişkeninin her karakterini ayrı olarak kopyalar ve print'le değişkendeki ismin harflerini alt alta yazar.
    print(y)

for z in mytuple: # tuple listesinin parantez içerisindeki elemanlarını olduğu gibi yazar.
    print(z)

for a,b in mytuple: #tuple içerisinde listelerin a ve b elemanlarını teker teker kopyalar ve paranteziz şekilde yazdırır.
    print(a,b)

for c in my_dict.keys(): #sözlük içerisindeki anahtar kelimeleri alır.
    print(c)

for d in my_dict.values(): #sözlük içerisindeki elemanları alır.
    print(d)

for k,s in my_dict.items(): #sözlük içerisindeki anahtar kelimeleri ve karşılıklarını birlikte alır.
    print(k,s)