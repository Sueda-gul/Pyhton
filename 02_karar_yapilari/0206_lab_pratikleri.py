#region ornek_1
""" 
bavulAgirligi = int(input('Lütfen Bavul Ağırlını Giriniz : '))
biletFiyat = float(input("Lütfen Bilet Fİyatını Giriniz : "))
if bavulAgirligi > 15:
    fark = bavulAgirligi - 15
    biletFiyat += fark*5
print(f"güncel bilet fiyatı {round(biletFiyat*1.18, 2)} TL.")
"""
#endregion

#region ornek_2
"""
bavulAgirligi = int(input('Lütfen Bavul Ağırlını Giriniz : '))
biletFiyat = float(input("Lütfen Bilet Fİyatını Giriniz : "))
ekUcret = 0
if bavulAgirligi > 15:
    ekUcret = (bavulAgirligi - 15) * 5
   
print(f"Toplam Ucret : {round((biletFiyat + ekUcret) *1.18, 2)} ")
print(f"KDV Ucreti : {round((biletFiyat + ekUcret) * 0.18, 2)}")
print(f"Ekstra Bagaj Ucreti : {ekUcret}")
"""
#endregion

#region ornek_3
""" 
bavulAgirligi = int(input('Lütfen Bavul Ağırlını Giriniz : '))
biletFiyat = float(input("Lütfen Bilet Fİyatını Giriniz : "))
if bavulAgirligi > 15:
    fark = (bavulAgirligi - 15)*5
    biletFiyat += fark
    print(f"{bavulAgirligi -15} ekstra ağırlık için {fark} TL ödediniz..")
print("Ödenecek olan tutar : ", biletFiyat*1.18, "TL")
"""
#endregion

#region ornek_4
# mutlak değer
"""
sayi = int(input("Lütfen Bir Sayı Giriniz : "))
if sayi<0:
    sayi *= -1
print(f"Sayının Mutlak Değeri : {sayi}")

"""
#endregion
#region ornek_5
#para transferi
"""
bakiye = 5000
bankaKodu = 101
eftBankaKodu = int(input("Lütfen transfer edilecek banka kodunu giriniz : "))
kesinti = 0
transfer = float(input("Lütfen eft tutarını giriniz : "))
if bankaKodu != eftBankaKodu:
    kesinti = transfer*0.05
print(f"Güncel bakiyeniz : {bakiye - transfer - kesinti}")
"""
#endregion

#region ornek_6
# 3 sayıdan büyük olanı yazılması
"""
eb = -900000
s =  int(input("Lütfen bir sayı giriniz    : "))
if eb < s:
    eb = s
s =  int(input("Lütfen bir sayı giriniz    : "))
if eb < s:
    eb = s
s =  int(input("Lütfen bir sayı giriniz    : "))
if eb < s:
    eb = s
print(f"Girilen sayılardan en büyüğü {eb}'dir. ")
"""
#endregion

#region ornek_7
"""
s1 =  int(input("Lütfen ilk sayıyı giriniz    : "))
s2 =  int(input("Lütfen ikinci sayıyı giriniz : "))

if s1 > s2:
    print(f"{s1} > {s2}")

"""
#endregion

#region ornek_8
"""
s1 =  int(input("Lütfen ilk sayıyı giriniz    : "))
s2 =  int(input("Lütfen ikinci sayıyı giriniz : "))
s3 =  int(input("Lütfen üçüncü sayıyı giriniz : "))

ort = (s1 + s2 + s3) / 3
if ort >= 50:
    print(f"GEÇTİNİZ, ORTALAMANIZ : {round(ort, 2)}")

"""
#endregion