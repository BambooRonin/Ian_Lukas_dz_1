choice = int(input('Введите число до 20 включительно: '))   # ввод числа для склонения
if choice % 10 == 1 and choice % 100 != 11:     # выяснение, не является ли число 1ой секндой
    print(choice, 'процент')
elif 1 < choice % 10 < 5 and not 11 < choice % 100 < 15:    # 2-4мя секундами
    print(choice, 'процента')
else:
    print(choice, 'процентов')                              # все остальные варианты
