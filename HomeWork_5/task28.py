# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
# 4 

def sum(a,b):
    if b==1:
        return 1
    return a+1+sum(0, b-1)

a=int(input('Введите целое неотрицательное число А: '))
b=int(input('Введите целое неотрицательное число В: '))

print(sum(a,b))