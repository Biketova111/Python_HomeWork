# Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

size = int(input("Введите количество элементов в списке: "))
list_1=[random.randint(0,100) for _ in range(size)]

num=int(input("Введите искоиое число: "))
count=list_1.count(num)


if count==0:
    blizkoe=list_1[0]
    for i in range(size):
        if abs(blizkoe-num)>abs(list_1[i]-num):
            blizkoe=list_1[i]

print(list_1)
print(f"Число {num} встречается в списке {count} раз")
print(f"Ближайшее значение всписке {blizkoe}")