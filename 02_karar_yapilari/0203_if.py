#region if_aciklama
"""
1- önce if yazılır
2- sonra koşul yazılır
3- sonra da : iki nokta ile blok başlatılır
"""
#endregion

#region ornek_1
"""
havaDurumu = "yağmurlu"

if havaDurumu == "yağmurlu":
    print("şemsiye alın lütfen")

print("a")
if(havaDurumu == "güneşli"):
    print("b")
print("c")
"""   
#endregion

#region ornek_2
"""
a = -10
if a < 0:
    print(f"{a} sayısı negatiftir")
"""
#endregion

#region ornek_3
"""
s = int(input("Lütfen sayı giriniz \t : "))
if s == 0:
    print("Lütfen 0 değeri girmeyin")
"""
#endregion

#region ornek_4
"""
uName = input("Lütfen Kullanıcı Adınızı Giriniz : ")
if uName != "admin":
    print(f"{uName} admin paneline giriş yapamaz!")
    print("Lütfen " + f"{uName} paneline geçiniz!!")
"""
#endregion