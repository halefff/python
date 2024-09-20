programlama_dilleri = ["Python","Javascript","Delphi","JAVA"] # programlama dilleri isminde bir liste oluşturuldu.

sonuc=programlama_dilleri
print(sonuc)
print(type(sonuc))


# Güncelleme İşlemi:
sonuc[-1] = "PHP"  #Son eleman olan JAVA'yı PHP olarak değiştirir
print(sonuc)

# Ekleme İşlemi:
sonuc=programlama_dilleri+["JQuery","HTML"]
print(sonuc)

# Silme İşlemi:
del programlama_dilleri[1]
print(programlama_dilleri)


# Koşul İşlemi:
sonuc="Python" in programlama_dilleri
print(sonuc) # Eğer "python" kelimesi var ise true, yok ise false değeri döndürür.