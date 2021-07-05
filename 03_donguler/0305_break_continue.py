# region break_continue_neden_kullanilir
""" 
break       → döngüyü sonlandırır
continue    → tepeye geri döner
"""
#endregion

#region break
""" 
i = 1
print("a")
while i<11:
    if i==5:
        print("b")      
        break
    print(f"{i}. döngü")
    i += 1
print("c")
"""
#endregion

#region continue
"""
i = 1
print("a")
while i < 11:
    if i == 5:
        i += 1     
        continue
    print(f"{i}. döngüdeyim")
    i += 1
print("b")
"""
#endregion

#region mix
""" 
i = 1
print("a")
while i < 100:
    if i % 7 == 0:
        i += 1
        continue  
    elif i % 16 == 0:     
        break
    print(f"{i}. döngüdeyim")
    i += 1
print("b")

"""
#endregion

#region ornek
"""
Kullanıcı istediği kadar sayı girsin. Çıkmak için -1 tuşuna bassın.
Döngü sonunda girilen en büyük sayıyı ekrana yazdıralım
Adım sayısı belli olmadığı için sonsuz döngü içerisinde çözümlenecek..

eb, sayac = 0, 0
while 0 == 0:
    sayi = int(input("Lütfen bir sayı giriniz, çıkmak için -1 tuşlayınız : "))
    if sayi == -1:
        break
    elif eb < sayi:
        eb = sayi
    sayac += 1
if sayac:
    print(f"Girilen en büyük sayı \t: {eb}")
else:
    print("Hiçbir sayı girmediniz!! ")
"""

#endregion
