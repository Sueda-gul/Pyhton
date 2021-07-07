# region ornek_1
""" 
Sonsuz döngüde : favori aylar girilecek
Daha önce ekledi ise uyaracak

favoriAylar = []
while True:
    favori = input("favori aynız, çıkmak için → 0 : ")
    if favori == "0":
        break
    if favori in favoriAylar:
        print("Daha önceden listeye eklenmiş, başka bir ay giriniz!!")
        continue
    favoriAylar.append(favori)    
for i in favoriAylar:
    print(i)
"""
# endregion

# region ornek_2
""" 
Keşisen liste örneği

liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]
ortak = []
for i in liste1:
    if i in liste2:
        ortak.append(i)
print(ortak)   
"""
# endregion

# region ornek_3
""" 
Birleşim Liste Örneği

stokDepo1 = [1, 2, 3, 4, 5]
stokDepo2 = [4, 5, 6, 7, 8]
stoklar = stokDepo1.copy()
for i in stokDepo2:
    if i not in stoklar:
        stoklar.append(i)
print(stoklar)

"""
# endregion
