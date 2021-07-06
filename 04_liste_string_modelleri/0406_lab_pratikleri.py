# region ornek_1
""" 
Listeye sonsuz döngü içinde öğrenci ekleyeceğiz

ogrenciListesi = []
while True:
    ogrenci = input("Listeye eklenecek öğrenci, çıkmak için -1 : ")
    if ogrenci == "-1":
        break
    ogrenciListesi.append(ogrenci)
# print(ogrenciListesi) 
for i in ogrenciListesi:
    print(i)  
"""
# endregion

# region ornek_2
""" 
Benzer örneği bu kez
EKle-Sil-Listele menüsü ile genişletelim

ogrenciListesi = []
print("""
# [1] → Ekle
# [2] → Sİl
# [3] → Listele
# [4] → Çık
""")
while True:
    secim = int(input("Lütfen bir seçim yapınız.. "))
    if secim == 1:
        ogrenci = input("Listeye eklenecek öğrenci : ")
        ogrenciListesi.append(ogrenci)
    elif secim == 2:
        ogrenci = input("Listeden silinecek öğrenci : ")
        adet = ogrenciListesi.count(ogrenci)
        if adet != 0:
            ogrenciListesi.remove(ogrenci)
        else:
            print(f"Listede {ogrenci} bulunmamaktadır, lütfen yeni bir seçim yapınız..")      
    elif secim == 3:
        for i in ogrenciListesi:
            print(i)
    elif secim == 4:  
        break
    else:
        print("Hatalı Secim..")

"""
# endregion

# region ornek_3
""" 
Ad-Soyad-Not1-Not2
sonsuz döngü içinde girilecek, not ortalamaları baz alınarak
en düşük, en yüksek not listelenecek

notOrtalamalari = []
eb, ek = 0, 9999999
while True:
    ogrenciAdSoyad = input("Lütfen Ad Soyad Giriniz, Çıkmak için -1 : ")
    if ogrenciAdSoyad == "-1":
        break
    n1 = int(input("LÜtfen 1. notunuzu giriniz : "))
    n2 = int(input("Lütfen 2. notunuzu giriniz : "))
    if not 0 <= n1 <= 100 or not 0 <= n2 <= 100:
        print("lütfen [0-100] arası bir değer girin")
        continue
    ort = round((n1 + n2)/2, 2)
    if eb < ort:
        eb = ort
        basarili = ogrenciAdSoyad
    if ek > ort:
        ek = ort
        basarisiz = ogrenciAdSoyad
    notOrtalamalari.append(ort)
print(f"Listedeki en yüksek not ortalaması → {max(notOrtalamalari)} {basarili} kişisine aittir")
print(f"Listedeki en düşük not ortalaması  → {min(notOrtalamalari)} {basarisiz} kişisine aittir")
"""

# endregion

# region ornek_4
"""
Benzer örneği bu kez
Çan eğrisi mantığı ile ortalamanın altında kalan notları listeleyelim

notOrtalamalari = []
eb, ek = 0, 9999999
while True:
    ogrenciAdSoyad = input("Lütfen Ad Soyad Giriniz, Çıkmak için -1 : ")
    if ogrenciAdSoyad == "-1":
        break
    n1 = int(input("LÜtfen 1. notunuzu giriniz : "))
    n2 = int(input("Lütfen 2. notunuzu giriniz : "))
    if not 0 <= n1 <= 100 or not 0 <= n2 <= 100:
        print("lütfen [0-100] arası bir değer girin")
        continue
    notOrtalamalari.append((n1 + n2)/2)
for i in notOrtalamalari:
    print(i)
print(f"en yüksek not → {max(notOrtalamalari)} - en şük not → {min(notOrtalamalari)}")
genelOrt = sum(notOrtalamalari)/len(notOrtalamalari)
for i in notOrtalamalari:
    if i < genelOrt:
        print(f"dönem tekrarı yapacak öğrencinin notu → {i}")
"""        
# endregion

# region ornek_5
""" 
iki basamaklı sayıyı → metne dönüştüreen uygulama yapınız..
örn: 95
doksan beş

birler =["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
yuzler = ["", "yüz", "iki yüz", "üç yüz","dört yüz", "beş yüz", "altı yüz", "yedi yüz", "sekiz yüz", "dokuz yüz"]
while True:
    sayi = int(input("en çok 3 basamaklı bir sayı giriniz, çıkmak için → -1  : "))
    if sayi == -1:
        break
    birlerB = sayi % 10
    onlarB = sayi // 10
    onlarB = onlarB % 10
    yuzlerB = sayi // 100
    print(yuzler[yuzlerB], onlar[onlarB], birler[birlerB])
"""
# endregion
