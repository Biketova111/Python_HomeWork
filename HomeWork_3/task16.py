# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1


n = int(input('Введите натуральное положительное число: '))
list_1=[i for i in range(1, n+1)]
print(list_1)
x=int(input('Введите число, количество которого необходимо найти в списке: '))
summ=0
for i in range(len(list_1)):
    if i == x:
        summ+=1
print(f'Число {x} встречается в списке {summ} раз')