# region ornek_1
""" 
sayı dizisi tanımlanacak
for loop içinde arama yaparak aradığınız ... indisli eleman bulundu mesajı verilecek

sayilar = [11, 5, 36, 78, 99, 2]
n = 0
for i in sayilar:
    if i == 99:
        break
    n += 1
print(f"aradığınız {n} indisli eleman bulundu ")

sayilar = [11, 5, 36, 78, 99, 2]
for i in range(len(sayilar)):
    if sayilar[i] == 99:
        print(f"aradığınız {i} indisli eleman bulundu ")
        break
"""
# endregion

# region ornek_2
""" 
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
Aradığınız Öğrenci: mehmet
mehmet isimli öğrenci bulundu
Aradığınız Öğrenci: murat
murat isimli öğrenci bulunamadı 

ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
isim = input("Aradığınız Öğrenci: ")
for i in range(len(ogrenciListesi)):
    if isim == ogrenciListesi[i]:
        print(f"{isim} isimli öğrenci bulundu.")
        break
else:
    print(f"{isim} isimli öğrenci bulunamadı.")

ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
while True:
    ogrenciAdi= input("Aradığınız Öğrenci İsmini Giriniz, Çıkmak için ç tuşlayınız : ")
    if ogrenciAdi == "ç":
        break
    for i in ogrenciListesi:
        if i == ogrenciAdi:
            print(f"{ogrenciAdi} isimli öğrenci bulundu")
            break
    else:
        print(f"{ogrenciAdi} isimli öğrenci bulunamadı")
"""
# endregion

# region ornek_3
""" 
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
Aradığınız Öğrenci: mehmet
mehmet listenin 3. sırasındaki öğrencidir
Aradığınız Öğrenci: murat
sınıfta murat isimli öğrenci yoktur 

ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa"]
while True:
    isim = input("Aradığınız Öğrenci İsmini Giriniz, Çıkmak için ç : ")
    if isim == "ç":
        break
    for i in range(len(ogrenciListesi)):
        if isim == ogrenciListesi[i]:
            print(f"{isim} listenin {i+1}. sırasındaki öğrencidir")
            break
    else:
            print(f"sınıfta {isim} isimli öğrenci yoktur")
"""
# endregion

# region ornek_4
""" 
ogrenciListesi = ["ali", "kemal", "mehmet", "mustafa", "önder"]
for i in range(len(ogrenciListesi)):
    print(ogrenciListesi[i], end=" ")
"""
# endregion