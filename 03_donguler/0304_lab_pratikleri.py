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
