# region append→eleman_ekler_listenin_sonuna
""" 
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"{meyveler} listenin ilk hali")
meyveler.append("karpuz")
print(f"{meyveler} listenin son hali")
"""
# endregion

# region insert→eleman ekler istediğiniz indekse
""" 
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"{meyveler} listenin ilk hali")
# meyveler.insert(2, "portakal") # doğru yöntem
# meyveler.insert("portakal", 2) # hatalı yöntem
meyveler.insert(99, "portakal")
print(f"listemizin son hali → {meyveler}")
"""
# endregion

# region remove→listeden_siler
"""
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"{meyveler} listenin ilk hali")
# meyveler.remove("muz")
meyveler.remove("muzz")
print(f"listemizin son hali {meyveler}")
"""
# endregion

# region pop→listeden_siler
""" 
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"{meyveler} listenin ilk hali")
# print(meyveler.pop()) # son elemanoı siler
print(meyveler.pop(2)) # o indeksli elemanı siler
print(f"listemizin son hali → {meyveler}")
sebzeler = []
sebzeler.pop() # IndexError
"""
# endregion

# region clear→listeyi_temizler
""" 
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"{meyveler} listenin ilk hali")
meyveler.clear()
print(meyveler)
del meyveler
print(f"listemizin son hali {meyveler}")
"""
# endregion

# region copy→listeyi_kopyalar
""" 
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
print(f"{meyveler} listenin ilk hali")
meyveTabagi = meyveler.copy()
print(f"listemizin son hali {meyveTabagi}")
"""
# endregion

# region count→eleman_sayisi
""" 
listeRakamlar = [2, 5, 6, 1, 9, 7, 5]
arananEleman = 5
elemanAdedi = listeRakamlar.count(arananEleman)
print(f"listemizdeki {arananEleman} elemanı adedi → {elemanAdedi}")
meyveler = ["elma", "armut", "muz", "ayva", "üzüm", "muz"]
print(meyveler.count("muzz"))
"""
# endregion

# region ornek_1
""" 
meyveler = ["elma", "armut", "muz", "ayva", "üzüm"]
arananMeyve = input("Aramak istediğiniz meyve? : ")
elemanAdedi = meyveler.count(arananMeyve)
if elemanAdedi: # elemanAdedi !=0
    print(f"aradığınız {arananMeyve} listede yer almaktadır.")
else:
    print(f"aradığınız {arananMeyve} listede yer almamaktadır.")
"""
# endregion

# region sort_reverse→sirala_tersten_sirala
""" 
listeRakamlar = [2, 5, 6, 1, 4, 9, 3, 8, 7]
print(f"listemizin ilk hali → {listeRakamlar}")
listeRakamlar.sort()
print(f"listemizin son hali → {listeRakamlar}")
listeRakamlar.reverse()
print(f"listemizin son hali → {listeRakamlar}")
"""
# endregion

# region index→arama_indeks_dondurme
""" 
listeRakamlar = [2, 5, 6, 1, 4, 9, 3, 8, 7]
print(listeRakamlar.index(10))
"""
# endregion