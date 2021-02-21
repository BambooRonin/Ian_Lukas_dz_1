n = []  # создаем список и возводим все его элементы в куб
for i in range(1, 1001, 2):
    n.append(i ** 3)
print(n)


sum_of_seven = 0
for idx, num in enumerate(n):  # вычисляем сумму всех элементов списка, чьи цифры в сумме делятся без остатка на 7
    sum_of_parts = 0
    while num > 0:
        sum_of_parts += num % 10
        num //= 10
    if sum_of_parts % 7 == 0:
        sum_of_seven += n[idx]
print(sum_of_seven)

for ind in range(len(n)):  # плюсуем 17 к каждому элементу списка n
    n[ind] += 17
print(n)


sum_of_seven = 0
for idx, num in enumerate(n):  # повторение для выщитывания измененного списка
    sum_of_parts = 0
    while num > 0:
        sum_of_parts += num % 10
        num //= 10
    if sum_of_parts % 7 == 0:
        sum_of_seven += n[idx]
print(sum_of_seven)
