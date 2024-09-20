#and=ve
#or=veya
#not=değil

x=11

sonuc=x>12   # x(yani 11 sayısı) 12den büyük olmadığı için false değeri döndürür.
sonuc2=x<12  # x(yani 11 sayısı) 12den küçük olduğu için true değeri döndürür.
print(sonuc,sonuc2)

# 1-and:
sonuc3 = (x<12) and (x==10)  #and değeinde iki koşulun da sağlanması gerektiği için false değeri dönürülür
print("sonuç 3:" + str(sonuc3)) #sonuc 3 bir boolean değeri olduğu için string'e çevirmek zorundayız.


# 2-or:
sonuc4 = (x<12) or (x>20)
print("sonuç 4:" + str(sonuc4))


# 3-not:
sonuc5 = not (x>9) #x 9'dan büyük değil diyoruz. yani false değeri vermeli.
print("sonuç 5:" + str(sonuc5))