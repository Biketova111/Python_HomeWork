# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.



s = int(input('Введите сумму чисел, задуманныз Петей: '))
p = int(input('Введите произведение чисел, задуманныз Петей: '))

for i in range(1000):
    for j in range(1000):
        x=i
        y=j
        if s == x+y and p == x*y:
            print(f'Задуманные Петей числа - это х = {x} и у = {y}')
