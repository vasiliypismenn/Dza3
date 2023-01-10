#1.1	1.	Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint
#import numpy

number = int(input('Введите размер списка '))
spis = []
spis2 = []

for i in range(number):
    spis.append(randint(0, 100)/10)
max = 0
min = 100  
print('исходный список')
print(spis)
print(' список дробной части ')

for i in range(number):
    c = (spis[i]) - (int(spis[i]))
    c = round(c,2)
    if c > max:
        max = c
    if c < min:
        min = c 
    
    print(c)

print ("Максимальные и минимальные значения равны",max,' и ',min)
razn = max - min
razn = round(razn,2)
print("Разница между максимальным и минимальным значением дробной части элементов  ", razn)
   