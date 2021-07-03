#region infinite_loop → sonsuz döngü
""" 
eb = -999999999
sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1'e basınız \t : "))
while sayi != -1:
    if sayi>eb:
        eb = sayi
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için -1'e basınız \t : "))
print(f"En büyük sayı : {eb}") 
""" 
#endregion

#region ornek_1
""" 
tekSayilarinAdedi, ciftSayilarinAdedi = 0, 0
sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0'a basınız \t : "))
while sayi != 0:
    if sayi% 2 == 0:
        ciftSayilarinAdedi += 1
    else:
        tekSayilarinAdedi += 1
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0'a basınız \t : "))
print(f"girdiğiniz sayılar içerisinde {tekSayilarinAdedi} adet tek sayı var..")
print(f"girdiğiniz sayılar içerisinde {ciftSayilarinAdedi} adet çift sayı var..") 
"""

#endregion

#region ornek_2
""" 
tekSayilarinToplami, ciftSayilarinToplami = 0, 0
sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0'a basınız \t : "))
while sayi != 0:
    if sayi% 2 == 0:
        ciftSayilarinToplami += sayi
    else:
        tekSayilarinToplami += sayi
    sayi = int(input("lütfen bir sayı giriniz, çıkmak için 0'a basınız \t : "))
print(f"girdiğiniz sayılardan tek sayıların toplamı {tekSayilarinToplami}'dır..'")
print(f"girdiğiniz sayılardan çift sayıların toplamı {ciftSayilarinToplami}'dır..") 
"""
#endregion