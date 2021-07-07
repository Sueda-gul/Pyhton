# region cok_boyutlu_listeler_giris
""" 
Matris yapıları oluşturma
veri tabanı mimarisine benzer satır x sütun yapıları oluşturma
"""
# endregion

# region cok_boyutlu_listeler_giris
"""
Örn kurum içi bilgisayarların özelliklerini tutacağınız bir tablo
Bil.No  Cihaz Adı       CPU     PID
1       Deskop_Test     %56     chrome.exe
2       Guest101        %60     excel.exe
3       Kat-1_Laptop    %90     camtasia.exe, chrome.exe
"""
# endregion

# region tanimlama
""" 
1 2 3 4 
5 6 7 8

i x j = 2 x 4

a = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(a)
"""
# endregion

# region erisim
""" 
a = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(a)
print(a[1])
print(a[0][2])
"""
# endregion

# region ornek
""" 
kurumBil = [
    [1, "Kat1 - PC", 45, "chrome.exe"],
    [2, "Deskop-Lab1", 84, "chrome.exe, camtasia"],
    [3, "Misafir-PC", 25, "excel.exe"]
]
print(kurumBil)
print(kurumBil[2])
print(kurumBil[1][1])
if kurumBil[1][2]>80:
    print(kurumBil[1][3])
"""
# endregion

# region for_ile_erisim_1
""" 
a = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15]]
# print(len(a[1])) # 2. satırın uzunluğu
for i in range(len(a)):
    for j in range(len(a[i])):
        print(f"{a[i][j]}", end="\t")
    print()

"""
# endregion

# region for_ile_erisim_2
""" 
kurumBil = [
    [1, "Kat1 - PC", 45, "chrome.exe"],
    [2, "Deskop-Lab1", 84, "chrome.exe, camtasia"],
    [3, "Misafir-PC", 25, "excel.exe"]
]
print(f"satır sayısı → {len(kurumBil)}")
print(f"sütun sayısı → {len(kurumBil[0])}")

for i in range(len(kurumBil)):
    for j in range(len(kurumBil[i])):
        print(f"{kurumBil[i][j]}\t", end="")
    print()
"""
# endregion
