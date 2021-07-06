# region yer_degistirme
""" 
listem = [1, 2, 3, 4, 5]
temp = listem[2]
listem[2] = listem[3]
listem[3] = temp
print(listem)
listem[2], listem[3] = listem[3], listem[2] 
print(listem)
"""
# endregion

# region slice
""" 
liste = ["a1", "a2", "a3"] # iterable
ad = "ecodation" # iterable
print(ad[0])

print("www.azizbektas.com"[0:3])
print("www.azizbektas.com"[-3:])

meyveler = ["elma", "armut", "üzüm", "muz", "şeftali", "erik"]
print(meyveler[0:4])
print(meyveler[-2:])
print(meyveler)
print(meyveler[:])
print(meyveler[-1:])
print(meyveler[1:5])
print(meyveler[1:5:1])
print(meyveler[1:5:2])
print(meyveler[1:15:2]) # index out of range but no problem
print(meyveler[:3])
"""
# endregion

# region slice_ornek
""" 
url = input("Lütfen site adı giriniz : ")
if not url[-3:] == "com" or not url[0:3] =="www":
    print("lütfen url formantına dikkat ediniz")
else:
    print(f"İnternet adresi → {url}")
"""
# endregion