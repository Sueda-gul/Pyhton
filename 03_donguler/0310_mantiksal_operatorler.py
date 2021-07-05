# mantıksal operatörler → logical operatörler
# koşul ifadelerini birleştirmek kullanılır
"""
1 → ve      and
2 → veya    or
3 → değil   not
"""

# region and
"""
print(5 == 5 and 15 > 5)
print(5 == 5 and 15 < 5)
print(5 == 15 and 15 > 5)
print(5 == 15 and 15 < 5)
"""

# endregion

# region or

""" 
print(5 == 5 or 15 > 5)
print(5 == 5 or 15 < 5)
print(5 == 15 or 15 > 5)
print(5 == 15 or 15 < 5)
"""

# endregion

# region not
""" 
print(not 5 == 5)
print(5 != 5)
"""
# endregion

# region ornek_1
""" 
iç içe if ile yapılan pratiği tekrar edelim
0 < sayı < 100 arasında pozitiftir

a = int(input("a değerini giriniz : "))
if a>0 and a<100:
    print(f"{a} sayısı 100'den küçük ve pozitiftir")

if 0 < a < 100:
    print(f"{a} sayısı 100 den küçük pozitiftir")

"""    
# endregion 

# region ornek_2
""" 
code.org  sitesine giriş yapacak olan kullanıcı
4, 5, 6 yaşları için kurs 1'e hoş geldin
dışında yaşı olanlar ise kurs 1'e uygun değilsin mesajı verelim

yas = int(input("Lütfen yaş bilgisini giriniz : "))
if yas > 6 or yas < 4:
    print("Kurs 1 için uygun değilsiniz, sorry :(")
else:
    print("Kurs 1'e hoş geldin ufaklık ☺")
"""

#endregion

# region ornek_3
"""
toplam = 0
while True:
    sayi = int(input("Lütfen çift sayı giriniz, çıkmak için 0 tuşlayınız : "))
    if sayi == 0:
        break
    if sayi < 0 or sayi % 2 != 0:
        print("Negatif veya tek sayı giremezsiniz !!")
        continue
    toplam += sayi
print(toplam)
"""

# endregion
