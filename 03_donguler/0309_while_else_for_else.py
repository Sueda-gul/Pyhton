# region while-else
# WHILE döngüsü BREAK satırı ÇALIŞARAK biterse, else içerisine GİRMEZ
# WHILE döngüsü BREAK satırı ÇALIŞMADAN biterse, else içerisine GİRER

"""
i = 1
while i<=10:
    print(i, end = " ")
    i += 1
    if i == 2:
        pass
        #break

else:
    print("Şuan else içerisine girdim")
print("while döngüsü bitti")
"""
# endregion

# region for-else
# FOR döngüsü BREAK satırı ÇALIŞARAK biterse, else içerisine GİRMEZ
# FOR döngüsü BREAK satırı ÇALIŞARAK biterse, else içerisine GİRMEZ
"""

for i in range(10, 1, -1):
    print(i, end=" ")
    if i == 9:
        break
else:
    print("şuan for elsedeyim")
print("brdym")

"""
# endregion


searchID = -1
for orderID in range(1, 100000):
    if orderID == searchID:
        print(f"{searchID} nolu sipariş detay listesi")
        print("...")
        break
else:
    print(f"{searchID} nolu sipariş için kayıt bulunamadı")