# region for_giris
""" 
for i in range(10):
    print(i, end = " ")
"""
# endregion

# region range
""" 
sayiDizisi = list(range(10)) #[0,10)
print(sayiDizisi)
"""
"""
sayiDizisi = list(range(5, 15, 1))  # [5,15) , 1 artış miktarıdır..
print(sayiDizisi)
"""
"""
sayiDizisi = list(range(15, 5, -1))  # [15,5) , 1 azalış miktarıdır..
print(sayiDizisi)
"""
# endregion

# region ornek_1
""" 
for i in range(1,11):
    if i != 5:
        print(f"{i}. Öğrenci")
"""
# endregion

# region ornek_2
""" 
for i in range(1,6):
    for j in range(1,6):
        print("* ", end = " ")
    print()

Aşağıdaki çıktıyı elde eden programı for yapısı ile oluşturunuz.

[1 x 1 = 1]     [1 x 2 = 2]     [1 x 3 = 3]     [1 x 4 = 4]     [1 x 5 = 5]
[2 x 1 = 2]     [2 x 2 = 4]     [2 x 3 = 6]     [2 x 4 = 8]     [2 x 5 = 10]
[3 x 1 = 3]     [3 x 2 = 6]     [3 x 3 = 9]     [3 x 4 = 12]    [3 x 5 = 15]

for i in range(1,4):
    for j in range(1,6):
        print(f"[{i} x {j} = {i*j}]", end = "\t")
    print()
"""
# endregion

# region pass
""" 
for i in range(1,6):
    for j in range(1,6):
        pass
"""
# endregion
