# region ornek_1
"""
Kullanıcı sayı girecek
int dönüşümü yapılacak
girilen sayının tam bölenleri ekrana yazdırılacak

sayi = int(input("Lütfen bir sayı giriniz : "))
print("Girilen sayının tam bölenleri :", end="  ")
for i in range(1, sayi + 1):
    if sayi % i == 0:
        print(f"{i}", end="  ")

"""
# endregion

# region ornek_2
"""
girilen sayıya kadar olan asal sayıları ekrana yazdıran program
kullanıcı sayı girecek

sayi = int(input("Lütfen bir sayı giriniz : "))
tutucu = 0
for i in range(2, sayi + 1):
    for j in range(1, i):
        if i % j == 0:
            tutucu += 1
    if tutucu == 1:
        print(i, end = "  ")
    tutucu = 0
"""
#endregion 

# region ornek_3
""" 
OBEB uygulaması

obeb = 0
3
s1 = int(input("Lütfen 1. sayıyı giriniz : "))
s2 = int(input("Lütfen 2. sayıyı giriniz : "))
for i in range(1, min(s1, s2) + 1):    
        if s1 % i == 0 and s2 % i == 0:
            obeb = i
print(obeb)
"""
# endregion

# region ornek_3
""" 
kullanıcının girdiği sayı TAU sayısı mıdır?
TAU sayısı : 
24 → 1, 2, 3, 4, 6, 8, 12, 24 → 24 % 8 == 0 TAU'dur.
15 → 1, 3, 5, 15 → 15 % 4 != 0 TAU değildir.
Anlamı : pozitif bölenlerin sayısına bakıldığında mod 0 ise TAU'dur

sayi = int(input("Lütfen bir sayı giriniz : "))
sayac = 0
for i in range(1, sayi + 1):
    if sayi % i == 0:
        sayac += 1 
if sayi % sayac == 0:
    print(f"{sayi} TAU sayısıdır.")
else:
    print(f"{sayi} TAU sayısı değildir.")
"""
# endregion

# region ornek_5
"""
mükemmel sayı kendisi haricindeki tüm çarpanlarının toplamı kendisini veren sayıdır
6  → 1, 2, 3 → toplamı 6 mükemmel sayıdır.
24 → 1, 2, 3, 4, 6, 8, 12 → toplamı 36 mükemmel sayı değildir.

sayi = int(input("Lütfen bir sayı giriniz : "))
toplam = 0
for i in range(1, int(sayi/2) + 1):
    if sayi % i == 0:
        toplam += i
if sayi == toplam:
    print(f"Girilen {sayi} Sayısı Mükkemel Sayıdır.")
else: 
    print(f"Girilen {sayi} Sayısı Mükkemel Sayı Değildir.")
"""
# endregion