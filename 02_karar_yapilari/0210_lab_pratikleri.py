#region ornek_1
""" 


n1 = int(input("Lütfen 1. sınav notunu giriniz \t : "))
n2 = int(input("Lütfen 2. sınav notunu giriniz \t : "))

ort = (n1 + n2) / 2
if ort >= 78:
    print(f"yıl sonu notunuz {ort}, başarı durumu AA, Geçtiniz")
elif ort>=74:
    print(f"yıl sonu notunuz {ort}, başarı durumu BA, Geçtiniz")
elif ort>=70:
    print(f"yıl sonu notunuz {ort}, başarı durumu BB, Geçtiniz")
elif ort>=65:
    print(f"yıl sonu notunuz {ort}, başarı durumu CB, Geçtiniz")
elif ort>=61:
    print(f"yıl sonu notunuz {ort}, başarı durumu CC, Geçtiniz")
elif ort>=58:
    print(f"yıl sonu notunuz {ort}, başarı durumu DC, Şartlı olarak geçtiniz")
elif ort>=52:
    print(f"yıl sonu notunuz {ort}, başarı durumu DD, Şartlı olarak geçtiniz")
elif ort>=47:
    print(f"yıl sonu notunuz {ort}, başarı durumu FD, KALDINIZ")
else:
    print(f"yıl sonu notunuz {ort}, başarı durumu FF, KALDINIZ")

"""
#endregion

#region ornek_2
""" 
s1 = int(input("Lütfen 1. sayıyı giriniz : "))
s2 = int(input("Lütfen 2. sayıyı giriniz : "))
s3 = int(input("Lütfen 3. sayıyı giriniz : "))

if s1<s2:
    s1, s2 = s2, s1
if s1<s3:
    s1, s3 = s3, s1   
if s2<s3:
    s2, s3 = s3, s2
print(f"büyükten küçüğe sıralama {s1}, {s2}, {s3}")
"""
#endregion

#region ornek_3
""" 
a = int(input("Lütfen a kenarını kenarını giriniz \t : "))
b = int(input("Lütfen b kenarını kenarını giriniz \t : "))
if a==b:
    print(f"karenin alanı {a*b}")
else:
    print(f"dikdörtegenin alanı {a*b}")
"""

#endregion

#region ornek_4
""" 
kısaKenar = int(input("Lütfen kısa kenarı kenarını giriniz \t : "))
uzunKenar = int(input("Lütfen uzun kenarı kenarını giriniz \t : "))
if kısaKenar>uzunKenar:
    print("kısa kenar uzun girilemez..")
else:
    print(f"dörtgenin çevresi {2*(kısaKenar + uzunKenar)}")
"""

#endregion

#region ornek_
""" 
a = int(input("Lütfen a sayısını kenarını giriniz \t : "))
b = int(input("Lütfen b sayısını kenarını giriniz \t : "))

if a%b == 0:
    print(f"{a} sayısı {b} sayısına tam bölünür")
else:
    print(f"{a} sayısı {b} sayısına tam bölünemez")
"""
#endregion