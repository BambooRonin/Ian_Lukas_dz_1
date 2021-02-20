given_seconds = int(input('Введите время в секундах: '))    # ввод преобразуемых данных
sec = given_seconds % 60    # вычисление секунд
min = (given_seconds // 60) % 60   # вычесление минут
hour = given_seconds // 3600    # вычисление часов
days = given_seconds // 86400   # вычисление дней
weeks = days * 7    # вычисление недель

print(weeks,'нед', days, 'дн', hour, 'ч', mins, 'мин', sec, 'сек')   # выдача результата
