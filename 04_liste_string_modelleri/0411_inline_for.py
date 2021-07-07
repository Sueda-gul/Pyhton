# region inline_for_giris
# tek satırda for yazmak mümkün
""" 
liste = []
for i in range(1,9):
    liste.append(i)
print(liste)

liste = [i for i in range(1,9)]
print(liste)

row = ["piyon" for i in range(8)]
print(row)
"""
# endregion

# region ornek
""" 
haftaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
Haftanın 1. Günü Pazartesi  Hatfanın 2. Günü Salı ...

haftaninGunleri = ["", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
liste = [f"Haftanın {i}. Günü {haftaninGunleri[i]}" for i in range(1, 8) if i<=3]
print(liste)
"""
# endregion