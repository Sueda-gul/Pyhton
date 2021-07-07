# region python_arama_metodlari
""" 
→ List index metodu: Liste elemanlarında arama yapar.
Bulduğu anda index'i geriye döndürür. Bulamazsa value error fırlatır. Try catch mekanizması ile doğru çalışabilir

→ List count metodu: tam olarak arama özelinde bir metod değildir.
Parametre ile gönderilen değerin, listede kaç adet olduğunu geriye döndürür. 0 → yoktur

→ In / Not In : bir diğer arama metodudur. Kullanımı oldukça basittir.
"""

# endregion

# region index
""" 
kurumAdi = "ecodation"
print(kurumAdi.index("i"))
"""
# endregion

# region index_ornek
""" 
meyveler = ["elma", "armut", "muz","ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz : ")
if meyveler.index(arananMeyve) >= 0:
    print("var")
"""
# endregion

# region count
""" 
kurum = "ecodation"
print(kurum.count("o"))
"""
# endregion

# region count_ornek
""" 
meyveler = ["elma", "armut", "muz","ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz : ")
if meyveler.count(arananMeyve) != 0:
    print("var")
else:
    print("yok")
"""    
# endregion

# region in_notin
""" 
kurum = "ecodation"
if "a" in kurum:
    print("vardır")
else:
    print("yoktur")
"""
# endregion

# region in_notin_ornek
""" 
meyveler = ["elma", "armut", "muz","ayva", "üzüm", "elma"]
arananMeyve = input("Lütfen Aradığınız Meyve İsmini Giriniz : ")
if arananMeyve in meyveler:
    print(f"{arananMeyve} liste elemanları içinde mevcut")
else:
    print(f"{arananMeyve} liste elemanları içinde yok")
"""
# endregion

# region tekrarsiz_liste
""" 
meyveler = ["elma", "armut", "muz","ayva", "üzüm", "elma"]
yeniListe = []
for i in meyveler:    
    if i not in yeniListe:
        yeniListe.append(i)
print(yeniListe)
"""
# endregion
