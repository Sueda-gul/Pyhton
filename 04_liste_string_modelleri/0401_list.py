# region list_giris
""" 
katilimciListesi = ["alperen","kübra","batu","umut"]
meyveler = ["karpuz","üzüm"]
plakalar = [34,35]
print(katilimciListesi,"\n", meyveler, "\n", plakalar)
"""
# endregion

# region bos_liste
""" 
isimler = []
print(isimler)
print(type(isimler))
plakalar = []
print(plakalar)

"""

# endregion

# region ornek_listeler
# dublicate???
""" 
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 15, "bakalım"] # farklı tipler bir arada olabiliyorr
print(sayilar)
ogrenciListesi = ["ali", "mustafa", "ali"]
print(ogrenciListesi)
"""

# endregion

# region index
""" 
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 12]
print(sayilar[1])
print(sayilar[0])
print(sayilar[7]) # çok doğru yaklaşım değill
print(sayilar[-1]) # son eleman
print(sayilar[-2])

"""
# endregion

# region guncelleme_degistime
""" 
sayilar = [11, 15, 7, 12]
print(sayilar)
sayilar[1] = 34
print(sayilar)
sayilar[1] = sayilar[3]
print(sayilar)
"""

# endregion

# region listenin_uzunlugu_eleman_sayisi
""" 
sayilar = [11, 15, 7, 12, 15, 25, 30]
print(len(sayilar))
print(sayilar[len(sayilar)-1])
print(sayilar[len(sayilar)//2])
"""
# endregion

# region del_talimati_instruction
"""
sayilar = [11, 15, 7, 12, 15]
print(sayilar)
del sayilar[1]
print(sayilar)
[11, 15, 7, 12, 15]
[11, 0, 7, 12, 15]
del sayilar #intellisense
print(sayilar)
""" 
# endregion

# region for_loop_ile_oku
""" 
sayilar = [12, 36, 9, 5, 3, 74]
print("30'dan büyük olan sayıların listesi")
for i in sayilar:
    if i>30:
        print(i)
"""
# endregion

# region for_loop_ile_elemanlarını_topla
""" 
toplam = 0
sayilar = [11, 15, 7, 12, 1, 0, 3.14, 15]
for i in sayilar:
    toplam += i
print(f"listedeki elemanların toplamı → {toplam}")
"""
# endregion

# region for_loop_ile_listedki_tek_sayi_adedi
""" 
adet = 0
sayilar = [11, 15, 7, 12, 1, 15]
for i in sayilar:
    if i % 2 != 0:
        adet += 1
print(f"listedeki tek sayıların adedi → {adet} ") 
"""
# endregion

# region for_loop_ile_listedki_tek_sayilarin_toplami
"""
toplam = 0
sayilar = [11, 15, 7, 12, 1, 15]
for i in sayilar:
    if i % 2 != 0:
        toplam += i
print(f"listedeki tek sayıların adedi → {toplam} ") 
"""
# endregion