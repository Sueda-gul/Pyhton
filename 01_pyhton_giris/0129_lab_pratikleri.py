#region pratikler
"""
print("
    LeyLek uygulamasına Hoş Geldiniz!!!
    Sürüş Ücreti → 0.59/dk
")
s = int(input("sürüş için geçen süre (saat)\t : "))
d = int(input("sürüş için geçen süre (dakika)\t : "))
toplamDakika = s*60
toplamDakika += d
toplamTutar = 0.59 * toplamDakika
print(f"Sürüş için geçen süre (saat)\t: {s}")
print(f"Sürüş için geçen süre (dakika)\t: {d}")
print(f"Sürüşün toplam süresi {s}:{d} - {toplamDakika} dakikada bitmiştir")
print(f"Kartınızdan çekilen toplam tutar {round(toplamTutar,2)}")

"""
#endregion

#region Odev_1
"""
km = int(input("Lütfen mesafe bilgisi giriniz (km)\t: "))
print(f"Gidilen mesafe {km} km = {round(km/1.609344,2)} mil'dir..")
print("-"*50)

#endregion

#region Odev_2

a = int(input("Lütfen Üçgenin A Kenarı Açısını Giriniz\t: "))
b = int(input("Lütfen Üçgenin B Kenarı Açısını Giriniz\t: "))
print(f"C kenarı {180-(a+b)} Deceredir")
print("-"*50)

#endregion
#region Odev_3

x1 = int(input("Birinci noktanın x koordinatı\t: "))
y1 = int(input("Birinci noktanın y koordinatı\t: "))
x2 = int(input("İkinci noktanın x koordinatı\t: "))
y2 = int(input("İkinci noktanın x koordinatı\t: "))
uzaklik = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
print(f"({x1},{y1}) ve ({x2},{y2}) noktaları arasındaki uzaklık {round(uzaklik,2)} birimdir.")

#endregion
#region Odev_4

at = int(input("Aylık tüketim giriniz? [kWh]\t: "))
aeb = at * 0.39736
db = aeb * 0.2474
teb = aeb + db
tp = 3.97
ef = 1.39
etv = 9.92
kdv = (teb + tp + ef + etv)*0.18
vt = tp + ef + etv + kdv
toplamFatura = vt + teb
print(f"Elektrik faturanız\t\t: {round(toplamFatura,2)}")

#endregion                  
#region Odev_5

gbe = float(input("Güncel Benzin Endeksini Giriniz\t\t  : "))
yt = float(input("Yakıt Tüketimini Giriniz [100 km. başına] : "))
yol = int(input("Kaç Kilometre Yol Aldınız?\t\t  : "))
print(f"Toplam Yakıt Tüketimi → {round(gbe*yt/100*yol,2)} ₺")

#endregion
#region Odev_6

urun = input("Lütfen Ürün Adı Giriniz\t\t\t: ")
adet = int(input(f"{urun} - Satın Alınacak Adet\t: "))
fiyat = float(input("Lütfen Ürün Fiyatı Giriniz [KDV-Dahil]  : "))
indirim = int(input("Lütfen İndirim Oranı Giriniz [%]\t: "))
print(f"Ürünlerin Toplam Tutarı {round(adet*fiyat*(1-indirim/100),1)} ₺")

#endregion
#region Odev_7
rakam = int(input("Lütfen bir rakam giriniz : "))
print(f"{rakam} + {rakam*11} + {rakam*111} → Sonuç: {rakam*123}")
"""
#endregion



#region Odev_8

sayi1 = int(input("Lütfen 3 basamaklı ilk sayıyı girin\t: "))
sayi2 = int(input("Lütfen 3 basamaklı ikinci sayıyı girin  : "))
sayi3 = int(input("Lütfen 3 basamaklı üçüncü sayıyı girin  : "))
print(f"Birler Basamakları Toplamı = {sayi1 % 10 + sayi2 % 10 + sayi3 % 10}")

#endregion
