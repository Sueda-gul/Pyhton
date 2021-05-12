#output adına casting - dönüşüm ile ilgili efor harcamamak için format yöntemleri kullanırız

#region format
#ekrana output formatlarken ilk yöntem → format
"""
rakam = int(input("lütfen 0-9 arası rakam giriniz\t: "))
print("girdiğiniz rakamın bir fazlası {}".format(rakam+1))
print("girdiğiniz {} rakamının bir fazlası {}".format(rakam, (rakam+1)))

a = int(input("Lütfen a değeri giriniz\t: "))
b = int(input("Lütfen b değeri giriniz\t: "))
print("{} ile {} değerinin toplamı = {}".format(a,b,a+b))
"""
#endregion

#region fstring
"""
rakam = int(input("Lütfen 0-9 arası bir rakam girniz\t: "))
print(f"girdiğiniz {rakam} rakamının bir fazlası {rakam+1}")

a = int(input("Lütfen a değeri giriniz\t: "))
b = int(input("Lütfen b değeri giriniz\t: "))
print(f"{a} ile {b} değerinin toplamı = {a+b}")
"""
#endregion

#region ornek
"""
a = int(input("Lütfen a değeri giriniz\t: "))
b = int(input("Lütfen b değeri giriniz\t: "))
print(f"{a} + {b} = {a+b}")
"""
#endregion