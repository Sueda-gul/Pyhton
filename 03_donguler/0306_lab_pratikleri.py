# region ornek_1
"""
1→ sonsuz döngü içinde kullanıcının girdiği sayıların tek olanlarının ortalamasını bulunuz
2→ çift sayı girmeye çalıştığında ekrana uyarı verilsin
3→ programda continue kullanılsın

i, toplam = 0, 0
while True:
    tekSayi = int(input("Lütfen tek sayı giriniz, çıkmak için -1'i tuşlayınız : "))
    if tekSayi == -1:
        break
    if tekSayi % 2 == 0:
        print("Çift sayı girmeyiniz!!")
        continue
    i += 1
    toplam += tekSayi
if i != 0:
    print(f"Girilen sayıların ortalaması : {round(toplam/i,2)}")
else:
    print("Hiç değer girilmedi!!")
"""
# endregion

# region ornek_2
"""
Kullanıcı aşağıdaki gibi bir seçim yaparak alt programları çalıştırınız
Hiçbiri değil ise hatalı seçim uyarısı veriniz
[1]     km → mil
[2]     mil → km
[3]     çık
"""

while True:
    secim = int(input("""
        [1]     km → mil
        [2]     mil → km
        [3]     çık
    """))
    if secim == 1:
        km = float(input("Lütfen km bilgisini giriniz \t :"))
        mil = km * 0.62137
        print(f"Girilen {km} değerinin mil hesaplaması {mil}")
    elif secim == 2:
        mil = float(input("Lütfen mil bilgisini giriniz \t :"))
        km = round(mil / 0.62137,2)
        print(f"Girilen {mil} değerinin km hesaplaması {km}")
    elif secim == 3:
        break
    else:
        print("Hatalı seçim")


# endregion
