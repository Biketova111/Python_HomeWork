# Задача 2: 
# Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


number = int (input('Введите трехначное число: '))
digit_1 = number//100
digit_2 = number%100//10
digit_3 = number%10

sumDigit = digit_1+digit_2+digit_3

print(f'Сумма цифр трехзначного числа, равна: {sumDigit}')