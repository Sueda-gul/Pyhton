# region siralama
""" 
orjinal liste   9, 7, 5, 1, 3, 4, 2, 6, 8
1. sıralamada   7, 5, 1, 3, 4, 2, 6, 8, 9
2. Sıralamada   5, 1, 3, 4, 2, 6, 7, 8, 9
3. Sıralamada   1, 3, 4, 2, 5, 6, 7, 8, 9
...

listem = [9, 7, 5, 1, 3, 4, 2, 6, 8]
sira = 1
while True:
    siraliMi = True
    for i in range(len(listem)-1):
        if listem[i] > listem[i+1]:
            listem[i], listem[i+1] = listem[i+1], listem[i]
            siraliMi = False
    print(f"{sira}. sıralamada   {listem}")
    sira += 1
    if siraliMi:
        break

"""
# endregion
