#1.5	Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.
# Пример:
#  для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Задайте число для составления списка чисел Фибоначчи: '))

def get_fibonacci(n):
    fibo_nums = []
    a = 1
    b = 1
    for i in range(1,n):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

print('список чисел Фибоначчи: ')
fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
#print(fibo_nums.index(0))
