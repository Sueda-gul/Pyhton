#region giris
# loop
# loop ne zaman kullanılır?
# loop → sürekli tekrarlayan işlemlerin yapılmasını sağlayan komutlar
"""
print("24 saatte kargoda ")
print("24 saatte kargoda ")
print("24 saatte kargoda ")


i = 0

while i<1000:
    i+=1
    print("24 saatte kargoda")
"""
#endregion

#region aman_dikkat
""" 
while True:
    print("şu an while döngüsü içindeyim")
"""    
#endregion

#region while_yazim_kurallari
""" 
1 → Başlagınç Değeri
2 → Bitiş Değeri
3 → Artış Miktarı 

i = 0
while i<3:
    i+=1
    print("24 saatte kargoda")
"""
#endregion

#region dikkat_edilmesi_gereken_kurallar
""" 
i = 0
while i>3: #döngüye girmez
    print("sponsorlu ürün")
    i += 1
i = 1
while i<3: #sonsuz döngü
    print("sponsorlu ürün")
"""
#endregion

#region ornek_1
""" 
i = 1
print("a")
while i<=3:
    print("b")
    if i==2:
        print("elif")
        i += 1
print("c")
"""
#endregion

#region ornek_2
""" 
i = 1
while i<=5:
    print(i)
    i += 1
"""
#endregion

#region ornek_3
""" 
sayac = 5
while sayac:
    print(sayac)
    sayac -= 1 

# def. da koşul bir tam sayıya bağlı olarak yazılırsa tam sayı 0 old. döngü kırılır..

sayac = 5
devamMi = True
while devamMi:
    print(sayac)
    if sayac == 2:
        devamMi = False
    sayac -= 1
"""
#endregion
