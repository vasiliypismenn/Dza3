#1.2	Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

from random import randint

number = int(input('Введите размер списка '))
spis = []
spis2 = []

for i in range(number):
    spis.append(randint(0, 10))

for i in range(len(spis)):
    while i < len(spis)/2 and number > len(spis)/2:
        number = number - 1
        a = spis[i] * spis[number]
        spis2.append(a)
        i += 1
print('исходный список')
print(spis)
print('результат произведения пар элементов ')
print(spis2)