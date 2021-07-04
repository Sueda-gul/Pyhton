#region ornek_1
""" 
metin = input("Lütfen Ekrana Yazdıralacak Metni Giriniz : ")
i = 0
while i<5:
    print(metin)
    i += 1
"""
#endregion

#region ornek_2
""" 
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * * * * * * * * * * 

i = 0
print(end = " ")
while i<10:
    print("* ", end = "")
    i += 1
"""
#endregion

#region ornek_3
""" 
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * $ * $ * $ * $ * $ 

i = 0
print(end = " ")
while i<10:
    if i%2 == 0:
        print("* ", end = "")
    else:
        print("$ ", end = "")
    i += 1
"""
#endregion

#region ornek_4
""" 
Aşağıdaki Pattern'i Python While Loop İle Yapınız
 * * * * * * * * * * 
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * * 
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * * 
 $ $ $ $ $ $ $ $ $ $
 * * * * * * * * * *
 $ $ $ $ $ $ $ $ $ $
i, j = 0, 0
while i<10:
    print(end =" ")
    while j<10:
        if i%2 == 0:
            print("* ", end = "")
        elif i%2 != 0:
            print("$ ", end = "")
        j += 1
    i +=1
    j = 0
    print()
"""
#endregion

#region ornek_5
"""
1→ [1-99] arası tek sayıların yan yana yazdıralım
2→ Her bir 10 adet sayıda alt satıra alalım

i , j = 1, 0
while i<100:
    while j < 10:
        if i%2 != 0:
            print(i,  end = "\t")
            j += 1
        i += 1
    j = 0
    print()
"""
#endregion

#region ornek_6
"""
1→ [1-99] arası tek sayıların toplamını yazdırınız..

i, toplam = 1, 0 
while i<100:
    toplam += i 
    i += 2
print(f"[1-99] arası tek sayıların toplamı : {toplam}")
"""
#endregion

#region ornek_7
"""
Lütfen Sayı Giriniz:    5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...

sayi = int(input("Lütfem Sayı Giriniz:\t"))
i = 1
while i<=10:
    print(f"{sayi} x {i} =", sayi*i)
    i += 1
"""
#endregion

#region ornek_8
"""
Kırk Haramilerin dolu mağarasından çıkmak için, gizli kelime olan susamı
bulmaya çalışan kahramanımızın hikayesini python ile yazalım
1→ kullanıcı gizli kelime girecek
2→ sonsuz döngü içinde kelimeyi bulmayı çalışırken, bulduğu anda döngüden çıkacak

kosul = True
while kosul:
    gizliKelime = input("Lütfen Gizli Kelimeyi Fısıldayınız: ")
    if gizliKelime == "susam":
        print("Kapı Açılıyor..")
        kosul = False
"""
#endregion

#region ornek_9
"""
Kullanıcıdan sonsuz döngü içinde sayı girmesi istenir. 0 girdiğinde döngüden çıkılacak.
1→ Döngü sonunda girilen sayıların ortalaması hesaplanacak.

i, sayi, toplam = -1, -1, 0
while sayi:
    sayi= int(input("Lütfen bir sayı giriniz : "))
    i += 1    
    toplam += sayi
    
print(f"Girilen sayıların ortalaması = {round(toplam/i,2)}")
"""
#endregion

#region ornek_10
"""
Kullanıcının girdiği rakama göre aşağıdaki gibi bir seri yazılacak
x - 2x - 3x - 4x - 5x
1→ kullanıcı rakam girecek
2→ int dönüşümü yapılacak
3→ döngü 5 kez tekrar ederek ekrandaki gibi bir çıktı yazıcalak
Lütfen [1-9] arası rakam giriniz:   4
4  8  12  16  20

sayi =int(input("Lütfen [1-9] arası rakam giriniz:  "))
i = 1
while i<=5:
    print(sayi*i, " ", end = "")
    i += 1
"""
#endregion

#region ornek_11
"""
1→ sayıların faktoriyelini bulacağız: [1-5]arası
2→ döngü 5 kez tekrar edecek
Çıktı:
1   1
2   2
3   6  
4   24
5   120

i, faktoriyel = 1, 1
while i<6:
    faktoriyel *= i
    print(f"{i}   {faktoriyel}")
    i += 1
"""
#endregion

#region ornek_12
"""
100-999 haneleri toplamı, hane sayısına eşit olanları ekrana yazalım
Koşulu Sağlayan Sayılar:
102 (3 haneli, haneleri toplamı 3)
111 (3 haneli, haneleri toplamı 3)
120 (3 haneli, haneleri toplamı 3)
201 (3 haneli, haneleri toplamı 3)
210 (3 haneli, haneleri toplamı 3)
300 (3 haneli, haneleri toplamı 3)

i = 100
print("**hane sayısı ve hanelerin toplamı birbirine eşit olan sayılar**")
while i<1000:
    sonHane = i%10
    ikinciHane = i//10 
    ikinciHane %= 10
    ilkHane = i//100
    hanelerinToplami = sonHane + ikinciHane + ilkHane
    if hanelerinToplami == 3:
        print(f"{i}")
    hanelerinToplami = 0
    i += 1
"""
#endregion

#region ornek_13
"""
rastgele [1-99] arası sayı üretilecek
kullanıcı 3 sayı girecek, en yakın tahmin ekrana yazılacak
örnek → 54
34
50
99
en yakın sayı 50

import random #random modülü
sayi = random.randint(1, 99) #[1-99] arası rassal integer sayı üretme
i, enKucukFark, enYakinTahmin = 0, 999999, 0 
while i<3:
    tahmin = int(input("Lütfen [1-99] arası bir tahmin giriniz : "))
    fark = sayi - tahmin
    if fark < 0:
        fark *= -1
    if fark < enKucukFark:
        enYakinTahmin = tahmin
        enKucukFark = fark
    i += 1

print("Üretilen Sayı : ", sayi)
print(f"Üretilen Sayıya En Yakın Tahmin : {tahmin} \nSayıdan Uzaklık : {fark}")
"""
#endregion

#region ornek_14
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız..
* * * * * * * * * *
* * * * * * * * * 
* * * * * * * *  
* * * * * * * 
* * * * * *  
* * * * *
* * * * 
* * * 
* * 
*
* 
* *
* * *
* * * * 
* * * * *
* * * * * *
* * * * * * * 
* * * * * * * * 
* * * * * * * * *
* * * * * * * * * *

i, j, k = 0, 10, 10
while i<10:
    while i<j: #j>0: olsun
        print("*", end =" ")
        j -= 1
    i += 1
    j = 10 # j = 10 - i olurdu
    print()
while i<20:
    while k<=i:
        print("*", end =" ")
        k += 1
    i += 1
    k = 10
    print()
"""
#endregion

#region ornek_15
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız..
* * * *
  * * *
    * *
      *
# ilk yöntem
i, j, n = 0, 4, 0
while i<4:
    while n>0:
        print(" ",end = " ")
        n -= 1
    while i<j:
        print("*", end =" ")
        j -= 1
    i += 1
    j = 4
    n = i
    print()
# ikinci yöntem
i, j, n = 0, 0, 0
while i<4:
    while j<4:
        if n<i:
            print(" ", end = " ")
        else:
            print("*", end = " ")
        j += 1
        n += 1
    i += 1
    j = 0
    n = 0
    print()
"""
#endregion

#region ornek_16
"""
Aşağıdaki Pattern'i Python While Loop İle Yapınız..
     *
    * *
   * * *
  * * * * 
 * * * * * 

i, j, k = 0, 0, 5
while i<5:
    while j<5:
        if k>1:
            print(" ", end ="")
        else:
            print("* ", end ="")
        k -= 1
        j += 1
    i += 1
    k = 5 - i
    j = 0
    print()
"""
#endregion
