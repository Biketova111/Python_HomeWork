# Задача 1: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

size_list1=int(input("Введите количество элементов первого множества: "))
size_list2=int(input("Введите количество элементов второго множества: "))

list_1=[]
list_2=[]

for i in range(size_list1):
    i=random.randint(0,10)
    list_1.append(i)
print(list_1)

for item in range(size_list2):
    item=random.randint(0,10)
    list_2.append(item)
print(list_2)

set_1=set(list_1)
set_2=set(list_2)

print(list(set_1.intersection(set_2)))


